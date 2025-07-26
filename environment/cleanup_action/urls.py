from django.urls import path

from .viewsets import CleanupActionFilterViewSet, CleanupActionViewSet

urlpatterns = [
    path(
        "organization-cleanup-action/<uuid:uuid>/",
        CleanupActionFilterViewSet.as_view({"get": "retrieve"}),
        name="organization-cleanup-action",
    ),
    path(
        "cleanup-action/",
        CleanupActionViewSet.as_view({"post": "create"}),
        name="cleanup-create",
    ),
    path(
        "cleanup-action/<uuid:uuid>/",
        CleanupActionViewSet.as_view({"get": "retrieve"}),
        name="cleanup-detail",
    ),
    path(
        "cleanup-actions/",
        CleanupActionViewSet.as_view({"get": "list"}),
        name="cleanup-list",
    ),
]
