from django.db import models


class PollutedArea(models.Model):
    uuid = models.UUIDField(
        unique=True,
        null=False,
        blank=False,
    )
    project_uuid = models.UUIDField(
        verbose_name="Project UUID",
        null=False,
        blank=False,
    )
    type_of_pollution = models.CharField(
        verbose_name="Type of pollution",
        choices=[
            ("water", "Water"),
            ("soil", "Soil"),
            ("waste", "Waste"),
            ("other", "Other"),
        ],
        default="other",
        max_length=20,
        null=True,
        blank=True,
    )
    pollution_level = models.CharField(
        verbose_name="Pollution level",
        choices=[
            ("low", "Low"),
            ("medium", "Medium"),
            ("high", "High"),
        ],
        default="medium",
        max_length=20,
        null=True,
        blank=True,
    )
    description = models.TextField(
        verbose_name="Pollution description",
        max_length=1000,
        null=False,
        blank=False,
    )
    location = models.CharField(
        verbose_name="Pollution location",
        max_length=255,
        null=False,
        blank=False,
    )
    created_at = models.DateTimeField(
        verbose_name="Created At",
        auto_now_add=True,
        null=True,
        blank=True,
    )
    updated_at = models.DateTimeField(
        verbose_name="Updated At",
        auto_now=True,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.type_of_pollution} pollution at {self.location}"
