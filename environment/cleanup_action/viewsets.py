import uuid

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from .models import CleanupAction
from .serializers import CleanupActionSerializer
from .extend_schema import (
    create_schema_decorator,
    get_by_id_schema_decorator,
    list_schema_decorator,
)


class CleanupActionFilterViewSet(viewsets.ModelViewSet):
    queryset = CleanupAction.objects.all()
    serializer_class = CleanupActionSerializer

    def retrieve(self, request, *args, **kwargs):
        org_uuid = kwargs.get("uuid")

        if not org_uuid:
            return Response(
                {"detail": "Organization UUID is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            org_obj = CleanupAction.objects.filter(org_uuid=org_uuid)
        except CleanupAction.DoesNotExist:
            raise NotFound(detail="Organization not found.")

        serializer = CleanupActionSerializer(org_obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CleanupActionViewSet(viewsets.ModelViewSet):
    queryset = CleanupAction.objects.all()
    serializer_class = CleanupActionSerializer
    lookup_field = "uuid"

    @create_schema_decorator
    def create(self, request, *args, **kwargs):
        new_uuid = uuid.uuid4()
        while CleanupAction.objects.filter(uuid=new_uuid).exists():
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
        return Response(serializer.data, status=status.HTTP_200_OK)
