from rest_framework import serializers

from .models import PollutionMeasurement


class PollutionMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollutionMeasurement
        fields = "__all__"
