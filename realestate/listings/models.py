from django_filters import rest_framework as filters
from django.db import models

from realestate.house_types.models import HouseType
from realestate.images.models import Image


class Listing(models.Model):
  title = models.CharField(max_length=200)
  address = models.CharField(max_length=200)
  description = models.TextField(blank=True)
  price = models.IntegerField(null=True)
  sqft = models.IntegerField(null=True)
  total_area = models.IntegerField(null=True)
  living_area = models.IntegerField(null=True)
  kitchen_area = models.IntegerField(null=True)
  floor = models.IntegerField(null=True)
  floor_in_house = models.IntegerField(null=True)
  type = models.ForeignKey(HouseType, on_delete=models.CASCADE, null=True)
  images = models.ManyToManyField(Image)


class ProductFilter(filters.FilterSet):
  min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
  max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

  class Meta:
    model = Listing
    fields = ['price']
