from django.urls import path

from .viewsets import CleanupActionViewSet

urlpatterns = [
    path(
        "cleanupactions/",
        CleanupActionViewSet.as_view({"get": "list"}),
        name="cleanup-list",
    ),
    path(
        "cleanupaction/",
        CleanupActionViewSet.as_view({"post": "create"}),
        name="cleanup-create",
    ),
    path(
        "cleanupaction/<uuid:cleanup_uuid>/",
        CleanupActionViewSet.as_view({"get": "retrieve"}),
        name="cleanup-detail",
    ),
]
