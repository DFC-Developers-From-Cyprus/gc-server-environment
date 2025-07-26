from django.urls import path

from .viewsets import PollutedAreaFilterViewSet, PollutedAreaViewSet

urlpatterns = [
    path(
        "location-polluted-area/<str:location>/",
        PollutedAreaFilterViewSet.as_view({"get": "retrieve"}),
        name="location-polluted-area-detail",
    ),
    path(
        "polluted-area/",
        PollutedAreaViewSet.as_view({"post": "create"}),
        name="polluted-area-create",
    ),
    path(
        "polluted-area/<uuid:uuid>/",
        PollutedAreaViewSet.as_view({"get": "retrieve"}),
        name="polluted-area-detail",
    ),
    path(
        "polluted-areas/",
        PollutedAreaViewSet.as_view({"get": "list"}),
        name="polluted-area-list",
    ),
]
