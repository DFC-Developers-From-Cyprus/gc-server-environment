from drf_spectacular.utils import (
    extend_schema,
    OpenApiParameter,
    OpenApiResponse,
    OpenApiTypes,
)

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

pollutionmeasurement_schema = {
    "type": "object",
    "properties": {},
}

get_by_id_schema_decorator = extend_schema(
    tags=["PollutionMeasurement"],
    responses={
        200: OpenApiResponse(
            response=pollutionmeasurement_schema,
        )
    },
)
