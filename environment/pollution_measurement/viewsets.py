import uuid

from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import PollutionMeasurement
from .serializers import PollutionMeasurementSerializer

from .extend_schema import (
    parameters_schema_decorator,
    get_by_id_schema_decorator,
)


class PollutionMeasurementViewSet(viewsets.ModelViewSet):
    queryset = PollutionMeasurement.objects.all()
    serializer_class = PollutionMeasurementSerializer

    @get_by_id_schema_decorator
    def retrieve(self, request, *args, **kwargs):
        pass
