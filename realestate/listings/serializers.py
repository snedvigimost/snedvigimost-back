from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework.serializers import ModelSerializer
from rest_framework_gis.serializers import GeoModelSerializer
from drf_extra_fields.geo_fields import PointField

from .models import Listing
from ..apartment_condition.serializers import ApartmentConditionSerializer
from ..bathroom_type.serializers import BathroomTypeSerializer
from ..districts.serializers import DistrictsSerializer
from ..heating_type.serializers import HeatingTypeSerializer
from ..house_types.serializers import HouseTypeSerializer
from ..images.serializers import ImageSerializer


class CreateListingSerializer(ModelSerializer):
    images = serializers.ListField(child=serializers.IntegerField(), allow_null=True, write_only=True)
    type = HouseTypeSerializer(read_only=True)
    heating_type = HeatingTypeSerializer(read_only=True)
    bathroom_type = BathroomTypeSerializer(read_only=True)
    apartment_condition = ApartmentConditionSerializer(read_only=True)

    class Meta:
        model = Listing
        fields = '__all__'


class ListingSerializer(FlexFieldsModelSerializer):
    images = ImageSerializer(read_only=True, many=True)
    type = HouseTypeSerializer(read_only=True)
    heating_type = HeatingTypeSerializer(read_only=True)
    bathroom_type = BathroomTypeSerializer(read_only=True)
    apartment_condition = ApartmentConditionSerializer(read_only=True)

    class Meta:
        model = Listing
        fields = '__all__'
        expandable_fields = {
            'district': DistrictsSerializer
        }


# class CreateListingSerializer(serializers.ModelSerializer):
#
#     def create(self, validated_data):
#         user = Listing.objects.create(**validated_data)
#         return user
#
#     class Meta:
#         model = Listing
#         fields = '__all__'
