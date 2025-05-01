import uuid

from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError

from .models import PollutionMeasurement
from .serializers import PollutionMeasurementSerializer
from polluted_area.models import PollutedArea

from .requests import get_air_quality
from .extend_schema import (
    parameters_schema_decorator,
    get_by_id_schema_decorator,
)


class PollutionMeasurementViewSet(viewsets.ModelViewSet):
    queryset = PollutionMeasurement.objects.all()
    serializer_class = PollutionMeasurementSerializer

    @get_by_id_schema_decorator
    def retrieve(self, request, *args, **kwargs):
        polluted_area_uuid = kwargs.get("uuid")
        polluted_area_object = get_object_or_404(PollutedArea, uuid=polluted_area_uuid)
        location = polluted_area_object.location

        additional_data = get_air_quality(location)
        if not additional_data:
            raise ValidationError(
                "It was not possible to get data on the quality of the air."
            )

        pollution_measurement_data = {
            "uuid": str(uuid.uuid4()),
            "polluted_area_uuid": polluted_area_uuid,
            "pollution_type": "NO2",
            "sensor_type": "Optical Sensor",
            "additional_data": additional_data,
        }

        serializer = self.get_serializer(data=pollution_measurement_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
