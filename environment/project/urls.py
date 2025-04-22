from django.urls import path

from .viewsets import ProjectViewSet

urlpatterns = [
    path(
        "project/",
        ProjectViewSet.as_view({"post": "create"}),
        name="project-create",
    ),
    path(
        "project/<uuid:uuid>/",
        ProjectViewSet.as_view({"get": "retrieve"}),
        name="project-detail",
    ),
    path(
        "projects/",
        ProjectViewSet.as_view({"get": "list"}),
        name="project-list",
    ),
]
