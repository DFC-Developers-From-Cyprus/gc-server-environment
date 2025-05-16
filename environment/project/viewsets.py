import uuid

from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Project
from .serializers import ProjectSerializer
from .extend_schema import (
    parameters_schema_decorator,
    list_schema_decorator,
    get_by_id_schema_decorator,
    create_schema_decorator,
)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = "uuid"

    @create_schema_decorator
    def create(self, request, *args, **kwargs):
        new_uuid = uuid.uuid4()
        while Project.objects.filter(uuid=new_uuid).exists():
            new_uuid = uuid.uuid4()

        data = request.data.copy()
        data["uuid"] = str(new_uuid)

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @get_by_id_schema_decorator
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @list_schema_decorator
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
