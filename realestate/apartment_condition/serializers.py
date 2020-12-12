from rest_framework import serializers
from .models import ApartmentCondition


class ApartmentConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentCondition
        fields = '__all__'
