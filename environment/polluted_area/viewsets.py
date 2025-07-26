import uuid

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from .models import PollutedArea
from .serializers import PollutedAreaSerializer
from .extend_schema import (
    list_schema_decorator,
    get_by_id_schema_decorator,
    create_schema_decorator,
)


class PollutedAreaFilterViewSet(viewsets.ModelViewSet):
    queryset = PollutedArea.objects.all()
    serializer_class = PollutedAreaSerializer
    lookup_field = "location"

    def retrieve(self, request, *args, **kwargs):
        location = kwargs.get("location")

        if not location:
            return Response(
                {"detail": "Location is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            location_obj = PollutedArea.objects.filter(location=location)
        except PollutedArea.DoesNotExist:
            raise NotFound(detail="Polluted area not found.")

        serializer = PollutedAreaSerializer(location_obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PollutedAreaViewSet(viewsets.ModelViewSet):
    queryset = PollutedArea.objects.all()
    serializer_class = PollutedAreaSerializer
    lookup_field = "uuid"

    @create_schema_decorator
    def create(self, request, *args, **kwargs):
        new_uuid = uuid.uuid4()
        while PollutedArea.objects.filter(uuid=new_uuid).exists():
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
