from rest_framework import serializers
from .models import BathroomType


class BathroomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BathroomType
        fields = '__all__'
