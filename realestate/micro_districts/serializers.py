from rest_framework import serializers
from .models import MicroDistricts


class MicroDistrictsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MicroDistricts
        fields = '__all__'
