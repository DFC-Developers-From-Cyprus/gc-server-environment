"""
URL configuration for environment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    path("A3Dm_iN-P3An6L/", admin.site.urls),
    path("", include("cleanup_action.urls")),
    path("", include("complaint.urls")),
    path("", include("polluted_area.urls")),
    path("", include("pollution_measurement.urls")),
    path("", include("project.urls")),
    path(
        "api/schema/",
        SpectacularAPIView.as_view(),
        name="schema",
    ),  # TODO Remove on deploy!
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),  # TODO Remove on deploy!
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),  # TODO Remove on deploy!
]
