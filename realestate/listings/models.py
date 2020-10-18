from django_filters import rest_framework as filters, BaseInFilter, NumberFilter, OrderingFilter
from django.db import models

from realestate.house_types.models import HouseType
from realestate.images.models import Image


class Listing(models.Model):
    title = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=200, null=True)
    source = models.CharField(max_length=200, null=True)
    publisher_type = models.CharField(max_length=200, null=True)
    year = models.CharField(max_length=5, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField(null=True)
    rooms_count = models.IntegerField(null=True)
    sqft = models.IntegerField(null=True)
    total_area = models.IntegerField(null=True)
    living_area = models.IntegerField(null=True)
    kitchen_area = models.IntegerField(null=True)
    floor = models.IntegerField(null=True)
    floor_in_house = models.IntegerField(null=True)
    type = models.ForeignKey(HouseType, on_delete=models.CASCADE, null=True)
    images = models.ManyToManyField(Image)
    publication_date = models.DateField(null=True)
    phone_number = models.CharField(max_length=200, null=True)
    is_published = models.BooleanField(default=False)


class NumberInFilter(BaseInFilter, NumberFilter):
    pass


class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    min_area = filters.NumberFilter(field_name="total_area", lookup_expr='gte')
    max_area = filters.NumberFilter(field_name="total_area", lookup_expr='lte')
    rooms_count = NumberInFilter(field_name="rooms_count", lookup_expr='in')

    sorting = OrderingFilter(
        fields=(
            ('total_area', 'total_area'),
            ('price', 'price'),
            ('publication_date', 'publication_date'),
        ),
    )

    class Meta:
        model = Listing
        fields = ['price', 'is_published', 'rooms_count', 'total_area']
