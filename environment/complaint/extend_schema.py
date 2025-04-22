from drf_spectacular.utils import (
    extend_schema,
    OpenApiParameter,
    OpenApiResponse,
    OpenApiTypes,
)

from .serializers import ComplaintSerializer

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

complaint_schema = {
    "type": "object",
    "properties": {},
}

list_schema_decorator = extend_schema(
    tags=["Complaint"],
    responses={
        200: OpenApiResponse(
            response=complaint_schema,
        )
    },
)

get_by_id_schema_decorator = extend_schema(
    tags=["Complaint"],
    responses={
        200: OpenApiResponse(
            response=complaint_schema,
        )
    },
)

create_schema_decorator = extend_schema(
    tags=["Complaint"],
    request=ComplaintSerializer,
    responses={
        200: OpenApiResponse(
            response=complaint_schema,
        )
    },
)
