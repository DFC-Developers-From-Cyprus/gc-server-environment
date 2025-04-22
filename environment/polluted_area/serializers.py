from rest_framework import serializers

from .models import PollutedArea


class PollutedAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollutedArea
        fields = "__all__"
