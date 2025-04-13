import uuid

from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import CleanupAction
from .serializers import CleanupActionSerializer
from .extend_schema import (
    parameters_schema_decorator,
    list_schema_decorator,
    get_by_id_schema_decorator,
    create_schema_decorator,
    update_schema_decorator,
)


class CleanupActionViewSet(viewsets.ModelViewSet):
    queryset = CleanupAction.objects.all()
    serializer_class = CleanupActionSerializer

    @list_schema_decorator
    def list(self, request, *args, **kwargs):
        pass

    @create_schema_decorator
    def create(self, request, *args, **kwargs):
        pass

    @get_by_id_schema_decorator
    def retrieve(self, request, *args, **kwargs):
        pass

    @update_schema_decorator
    def update(self, request, *args, **kwargs):
        pass
