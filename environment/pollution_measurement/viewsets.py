from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from .models import PollutionMeasurement
from .serializers import PollutionMeasurementSerializer
from polluted_area.models import PollutedArea

from .requests import get_air_quality
from .extend_schema import (
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
            raise ValidationError(404)

        pollution_measurement_data = {
            "polluted_area_uuid": polluted_area_uuid,
            "pollution_type": "NO2",
            "sensor_type": "Optical Sensor",
            "additional_data": additional_data,
        }

        serializer = self.get_serializer(data=pollution_measurement_data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
