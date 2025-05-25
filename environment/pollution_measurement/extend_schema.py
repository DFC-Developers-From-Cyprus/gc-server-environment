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
    "properties": {
        "polluted_area_uuid": {
            "type": "string",
            "format": "uuid",
            "description": "UUID загрязнённой зоны",
        },
        "pollution_type": {
            "type": "string",
            "enum": ["air", "waste", "water"],
            "default": "waste",
            "description": "Тип загрязнителя",
        },
        "sensor_type": {
            "type": "string",
            "enum": ["air"],
            "default": "air",
        },
        "additional_data": {
            "type": "object",
            "description": "Дополнительные данные, связанные с измерением",
        },
    },
    "required": ["polluted_area_uuid", "additional_data"],
}

get_by_id_schema_decorator = extend_schema(
    tags=["PollutionMeasurement"],
    responses={
        200: OpenApiResponse(
            response=pollutionmeasurement_schema,
        )
    },
)
