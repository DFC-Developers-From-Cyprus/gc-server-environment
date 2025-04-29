import uuid

from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import PollutionMeasurement
from .serializers import PollutionMeasurementSerializer
from polluted_area.models import PollutedArea

from .requests import test
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
        print(test(location))
        return Response(200)
