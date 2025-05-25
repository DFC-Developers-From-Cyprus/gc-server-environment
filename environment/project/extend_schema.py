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
    "properties": {
        "uuid": {
            "type": "string",
            "format": "uuid",
            "description": "Уникальный идентификатор проекта (UUID).",
        },
        "title": {
            "type": "string",
            "maxLength": 255,
            "description": "Название проекта. Должно быть уникальным.",
        },
        "description": {
            "type": "string",
            "maxLength": 1000,
            "description": "Подробное описание целей, задач и особенностей проекта.",
        },
        "created_by": {
            "type": "string",
            "format": "uuid",
            "description": "UUID пользователя, создавшего проект.",
        },
        "status": {
            "type": "string",
            "enum": ["active", "completed", "on_hold"],
            "default": "active",
            "description": "Статус проекта. Возможные значения: 'active' (активен), 'completed' (завершён), 'on_hold' (приостановлен).",
        },
        "location": {
            "type": "string",
            "maxLength": 255,
            "description": "Местоположение реализации проекта (город, район, координаты и т.д.).",
        },
        "start_date": {
            "type": "string",
            "format": "date-time",
            "description": "Дата начала проекта в формате ISO 8601. Устанавливается автоматически при создании записи.",
        },
        "end_date": {
            "type": "string",
            "format": "date-time",
            "description": "Дата окончания проекта в формате ISO 8601. Устанавливается автоматически при создании записи.",
        },
        "created_at": {
            "type": "string",
            "format": "date-time",
            "description": "Дата и время создания проекта в формате ISO 8601. Устанавливается автоматически.",
        },
        "updated_at": {
            "type": "string",
            "format": "date-time",
            "description": "Дата и время последнего обновления проекта в формате ISO 8601. Обновляется автоматически при каждом изменении.",
        },
    },
    "required": ["uuid", "title", "description", "created_by"],
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
        201: OpenApiResponse(
            response=project_schema,
        )
    },
)
