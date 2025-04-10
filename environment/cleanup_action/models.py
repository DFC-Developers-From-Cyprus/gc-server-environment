from django.db import models


class CleanupAction(models.Model):
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
        verbose_name="Description",
        null=False,
        blank=False,
    )
    photos = models.URLField(
        verbose_name="Photos",
        null=False,
        blank=False,
    )

    def __str__(self):
        return f"Cleanup by {self.user_uuid} on {self.action_date}"
