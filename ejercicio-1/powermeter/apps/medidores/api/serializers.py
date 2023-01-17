from rest_framework import serializers
from ..models import Measurer, Measurement

class MeasurerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Measurer
        fields=['key', 'name']


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model=Measurement
        fields=['consumption_kwh', 'measurer','created_at']
        read_only_fields=('created_at',)