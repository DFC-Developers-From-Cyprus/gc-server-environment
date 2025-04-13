from drf_spectacular.utils import (
    extend_schema,
    OpenApiParameter,
    OpenApiResponse,
    OpenApiTypes,
)

from .serializers import CleanupActionSerializer

parameters_schema_decorator = extend_schema(
    parameters=[
        OpenApiParameter(
            name="Authorization-ID",
            type=OpenApiTypes.UUID,
            location=OpenApiParameter.HEADER,
            required=True,
            description="Authorization token",
        ),
    ]
)

cleanupaction_schema = {
    "type": "object",
    "properties": {},
}

list_schema_decorator = extend_schema(
    tags=["CleanupAction"],
    responses={
        200: OpenApiResponse(
            response=cleanupaction_schema,
        )
    },
)

get_by_id_schema_decorator = extend_schema(
    tags=["CleanupAction"],
    responses={
        200: OpenApiResponse(
            response=cleanupaction_schema,
        )
    },
)

create_schema_decorator = extend_schema(
    tags=["CleanupAction"],
    request=CleanupActionSerializer,
    responses={
        200: OpenApiResponse(
            response=cleanupaction_schema,
        )
    },
)

update_schema_decorator = extend_schema(
    tags=["CleanupAction"],
    request=CleanupActionSerializer,
    responses={
        200: OpenApiResponse(
            response=cleanupaction_schema,
        )
    },
)
