from rest_framework import serializers
from .models import HeatingType


class HeatingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeatingType
        fields = '__all__'
