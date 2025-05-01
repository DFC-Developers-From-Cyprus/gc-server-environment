from django.db import models


class PollutionMeasurement(models.Model):
    uuid = models.UUIDField(
        unique=True,
        null=False,
        blank=False,
    )
    polluted_area_uuid = models.UUIDField(
        verbose_name="UUID of the polluted area",
        null=False,
        blank=False,
    )
    pollution_type = models.CharField(
        verbose_name="Type of pollutant measured",
        max_length=255,
        null=True,
        blank=True,
    )
    measurement_date = models.DateTimeField(
        verbose_name="Date and time when the measurement was taken",
        auto_now_add=True,
        null=True,
        blank=True,
    )
    sensor_type = models.CharField(
        verbose_name="Type of sensor",
        max_length=255,
        null=True,
        blank=True,
    )
    additional_data = models.JSONField(
        verbose_name="Any additional data (dictionary)",
        null=False,
        blank=False,
    )

    def __str__(self):
        return f"at {self.measurement_date}"
