from django.urls import path

from .viewsets import MeasurementViewSet

urlpatterns = [
    path(
        "polluted-area/<uuid:uuid>/measurements/",
        MeasurementViewSet.as_view({"get": "retrieve"}),
        name="measurement-detail",
    ),
]
