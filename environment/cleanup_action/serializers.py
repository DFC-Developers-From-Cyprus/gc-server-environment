from rest_framework import serializers

from .models import CleanupAction


class CleanupActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CleanupAction
        fields = "__all__"
