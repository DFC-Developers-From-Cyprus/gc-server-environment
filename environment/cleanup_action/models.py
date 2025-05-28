import uuid

from django.db import models


class CleanupAction(models.Model):
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
    action_date = models.DateTimeField(
        verbose_name="Action Date",
        auto_now_add=True,
        null=True,
        blank=True,
    )
    description = models.TextField(
        verbose_name="Action description",
        null=False,
        blank=False,
    )
    photos = models.URLField(
        verbose_name="Action photos",
        null=False,
        blank=False,
    )

    def __str__(self):
        return f"Cleanup by {self.user_uuid} on {self.action_date}"
