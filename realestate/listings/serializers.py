from rest_framework import serializers

from .models import Listing
from ..house_types.serializers import HouseTypeSerializer
from ..images.serializers import ImageSerializer


class ListingSerializer(serializers.ModelSerializer):
    images = ImageSerializer(read_only=True, many=True)
    type = HouseTypeSerializer(read_only=True)

    class Meta:
        model = Listing
        fields = '__all__'


class CreateListingSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = Listing.objects.create(**validated_data)
        return user

    class Meta:
        model = Listing
        fields = '__all__'
