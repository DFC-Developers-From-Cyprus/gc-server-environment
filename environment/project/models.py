from django.db import models


class Project(models.Model):
    uuid = models.UUIDField(
        unique=True,
        null=False,
        blank=False,
    )
    title = models.CharField(
        verbose_name="Project title",
        unique=True,
        max_length=255,
        null=False,
        blank=False,
    )
    description = models.TextField(
        verbose_name="Project description",
        max_length=1000,
        null=False,
        blank=False,
    )
    created_by = models.UUIDField(
        verbose_name="Created by (User UUID)",
        null=False,
        blank=False,
    )
    status = models.CharField(
        verbose_name="Project status",
        choices=[
            ("active", "Active"),
            ("completed", "Completed"),
            ("on_hold", "On Hold"),
        ],
        default="active",
        max_length=20,
        null=True,
        blank=True,
    )
    location = models.CharField(
        verbose_name="Project location",
        max_length=255,
        null=True,
        blank=True,
    )
    start_date = models.DateTimeField(
        verbose_name="Start date",
        auto_now_add=True,
        null=True,
        blank=True,
    )
    end_date = models.DateTimeField(
        verbose_name="End Date",
        auto_now_add=True,
        null=True,
        blank=True,
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
        return self.title
