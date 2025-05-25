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
    "properties": {
        "uuid": {
            "type": "string",
            "format": "uuid",
            "example": "123e4567-e89b-12d3-a456-426614174000",
            "description": "Уникальный идентификатор жалобы",
        },
        "project_uuid": {
            "type": "string",
            "format": "uuid",
            "example": "123e4567-e89b-12d3-a456-426614174001",
            "description": "UUID проекта, к которому относится жалоба",
        },
        "user_uuid": {
            "type": "string",
            "format": "uuid",
            "example": "123e4567-e89b-12d3-a456-426614174002",
            "description": "UUID пользователя, отправившего жалобу",
        },
        "location": {
            "type": "string",
            "maxLength": 255,
            "nullable": True,
            "example": "123 Main St, Springfield",
            "description": "Местоположение, связанное с жалобой",
        },
        "complaint_date": {
            "type": "string",
            "format": "date-time",
            "example": "2025-05-16T14:30:00Z",
            "readOnly": True,
            "description": "Дата создания жалобы",
        },
        "description": {
            "type": "string",
            "maxLength": 1000,
            "example": "На стройке сильный шум после 22:00.",
            "description": "Текст жалобы",
        },
        "status": {
            "type": "string",
            "enum": ["open", "pending", "resolved"],
            "example": "open",
            "description": "Статус жалобы",
        },
        "priority": {
            "type": "string",
            "enum": ["low", "medium", "high"],
            "example": "medium",
            "description": "Приоритет жалобы",
        },
        "photos": {
            "type": "string",
            "format": "uri",
            "example": "https://example.com/image1.jpg",
            "description": "URL с фотографиями, подтверждающими жалобу",
        },
    },
    "required": ["uuid", "project_uuid", "user_uuid", "description", "photos"],
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
        201: OpenApiResponse(
            response=complaint_schema,
        )
    },
)
