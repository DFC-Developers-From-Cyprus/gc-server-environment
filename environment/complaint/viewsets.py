import uuid

from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Complaint
from .serializers import ComplaintSerializer
from .extend_schema import (
    parameters_schema_decorator,
    list_schema_decorator,
    get_by_id_schema_decorator,
    create_schema_decorator,
)


class ComplaintViewSet(viewsets.ModelViewSet):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer

    @list_schema_decorator
    def list(self, request, *args, **kwargs):
        pass

    @create_schema_decorator
    def create(self, request, *args, **kwargs):
        pass

    @get_by_id_schema_decorator
    def retrieve(self, request, *args, **kwargs):
        pass
