from django_filters import rest_framework as filters
from django.db import models

class Listing(models.Model):
  title = models.CharField(max_length=200)
  address = models.CharField(max_length=200)
  description = models.TextField(blank=True)
  price = models.IntegerField(null=True)
  sqft = models.IntegerField(null=True)
  photo = models.FileField(upload_to='photos', null=True)

class ProductFilter(filters.FilterSet):
  min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
  max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

  class Meta:
    model = Listing
    fields = ['price']
