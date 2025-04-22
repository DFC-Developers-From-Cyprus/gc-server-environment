from django.urls import path

from .viewsets import ComplaintViewSet

urlpatterns = [
    path(
        "complaint/",
        ComplaintViewSet.as_view({"post": "create"}),
        name="complaint-create",
    ),
    path(
        "complaint/<uuid:uuid>/",
        ComplaintViewSet.as_view({"get": "retrieve"}),
        name="complaint-detail",
    ),
    path(
        "complaints/",
        ComplaintViewSet.as_view({"get": "list"}),
        name="complaint-list",
    ),
]
