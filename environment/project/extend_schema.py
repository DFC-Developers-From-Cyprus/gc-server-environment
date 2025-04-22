from drf_spectacular.utils import (
    extend_schema,
    OpenApiParameter,
    OpenApiResponse,
    OpenApiTypes,
)

from .serializers import ProjectSerializer

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

project_schema = {
    "type": "object",
    "properties": {},
}

list_schema_decorator = extend_schema(
    tags=["Project"],
    responses={
        200: OpenApiResponse(
            response=project_schema,
        )
    },
)

get_by_id_schema_decorator = extend_schema(
    tags=["Project"],
    responses={
        200: OpenApiResponse(
            response=project_schema,
        )
    },
)

create_schema_decorator = extend_schema(
    tags=["Project"],
    request=ProjectSerializer,
    responses={
        200: OpenApiResponse(
            response=project_schema,
        )
    },
)
