import uuid

from django.db import models


class Complaint(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    project_uuid = models.UUIDField(
        verbose_name="Project UUID",
        null=False,
        blank=False,
    )
    user_uuid = models.UUIDField(
        verbose_name="User UUID",
        null=False,
        blank=False,
    )
    location = models.CharField(
        verbose_name="Location",
        max_length=255,
        null=True,
        blank=True,
    )
    complaint_date = models.DateTimeField(
        verbose_name="Complaint Date",
        auto_now_add=True,
        null=True,
        blank=True,
    )
    description = models.TextField(
        verbose_name="Complaint description",
        max_length=1000,
        null=False,
        blank=False,
    )
    status = models.CharField(
        verbose_name="Complaint status",
        choices=[
            ("open", "Open"),
            ("pending", "Pending"),
            ("resolved", "Resolved"),
        ],
        default="open",
        max_length=50,
        null=True,
        blank=True,
    )
    photos = models.URLField(
        verbose_name="Complaint photos",
        max_length=2000,
        null=False,
        blank=False,
    )

    def __str__(self):
        return f"Complaint by {self.user_uuid} on {self.complaint_date}"
