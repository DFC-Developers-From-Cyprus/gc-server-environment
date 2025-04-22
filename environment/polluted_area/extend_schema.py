from drf_spectacular.utils import (
    extend_schema,
    OpenApiParameter,
    OpenApiResponse,
    OpenApiTypes,
)

from .serializers import PollutedAreaSerializer

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

pollutedarea_schema = {
    "type": "object",
    "properties": {},
}

list_schema_decorator = extend_schema(
    tags=["PollutedArea"],
    responses={
        200: OpenApiResponse(
            response=pollutedarea_schema,
        )
    },
)

get_by_id_schema_decorator = extend_schema(
    tags=["PollutedArea"],
    responses={
        200: OpenApiResponse(
            response=pollutedarea_schema,
        )
    },
)

create_schema_decorator = extend_schema(
    tags=["PollutedArea"],
    request=PollutedAreaSerializer,
    responses={
        200: OpenApiResponse(
            response=pollutedarea_schema,
        )
    },
)
