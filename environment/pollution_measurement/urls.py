from django.urls import path

from .viewsets import PollutionMeasurementViewSet

urlpatterns = [
    path(
        "polluted-area/<uuid:uuid>/measurements/",
        PollutionMeasurementViewSet.as_view({"get": "retrieve"}),
        name="pollution-measurement-detail",
    ),
]
