from rest_framework import serializers
from .models import Listing

class ListingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Listing
        fields = ('id', 'title', 'address', 'description', 'price', 'sqft',)


class CreateListingSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = Listing.objects.create(**validated_data)
        return user

    class Meta:
        model = Listing
        fields = ('id',  'title', 'address', 'description', 'price', 'sqft',)
