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
    "properties": {
        "uuid": {
            "type": "string",
            "format": "uuid",
            "description": "Уникальный идентификатор загрязнённой территории (UUID).",
        },
        "project_uuid": {
            "type": "string",
            "format": "uuid",
            "description": "Идентификатор проекта, к которому относится данная загрязнённая территория.",
        },
        "type_of_pollution": {
            "type": "string",
            "enum": ["water", "soil", "waste", "other"],
            "default": "other",
            "description": "Тип загрязнения. Возможные значения: 'water' (вода), 'soil' (почва), 'waste' (отходы), 'other' (другое).",
        },
        "pollution_level": {
            "type": "string",
            "enum": ["low", "medium", "high"],
            "default": "medium",
            "description": "Уровень загрязнения. Возможные значения: 'low' (низкий), 'medium' (средний), 'high' (высокий).",
        },
        "description": {
            "type": "string",
            "maxLength": 1000,
            "description": "Подробное описание характера загрязнения, его источников и последствий.",
        },
        "location": {
            "type": "string",
            "maxLength": 255,
            "description": "Физическое местоположение загрязнённой территории (например, координаты, адрес, район).",
        },
        "created_at": {
            "type": "string",
            "format": "date-time",
            "description": "Дата и время создания записи о загрязнении в формате ISO 8601.",
        },
        "updated_at": {
            "type": "string",
            "format": "date-time",
            "description": "Дата и время последнего обновления записи в формате ISO 8601.",
        },
    },
    "required": ["uuid", "project_uuid", "description", "location"],
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
        201: OpenApiResponse(
            response=pollutedarea_schema,
        )
    },
)
