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
    "properties": {
        "uuid": {
            "type": "string",
            "format": "uuid",
            "description": "Уникальный идентификатор действия",
        },
        "project_uuid": {
            "type": "string",
            "format": "uuid",
            "description": "UUID проекта, к которому относится действие",
        },
        "user_uuid": {
            "type": "string",
            "format": "uuid",
            "description": "UUID пользователя, выполнившего действие",
        },
        "action_date": {
            "type": "string",
            "format": "date-time",
            "description": "Дата и время выполнения действия (автоматически добавляется)",
        },
        "description": {"type": "string", "description": "Описание действия"},
        "photos": {
            "type": "string",
            "format": "uri",
            "description": "URL фотографии, связанной с действием",
        },
    },
    "required": ["uuid", "project_uuid", "user_uuid", "description", "photos"],
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
