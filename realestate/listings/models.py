from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django_filters import rest_framework as filters, BaseInFilter, NumberFilter, OrderingFilter, ModelChoiceFilter
from django.contrib.gis.db import models

from realestate.apartment_condition.models import ApartmentCondition
from realestate.bathroom_type.models import BathroomType
from realestate.districts.models import Districts
from realestate.heating_type.models import HeatingType
from realestate.house_types.models import HouseType
from realestate.images.models import Image
from realestate.layout.models import Layout
from realestate.micro_districts.models import MicroDistricts
from realestate.streets.models import Streets
from realestate.users.models import User


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
    house_type = models.ForeignKey(HouseType, on_delete=models.CASCADE, null=True)
    heating_type = models.ForeignKey(HeatingType, on_delete=models.CASCADE, null=True)
    bathroom_type = models.ForeignKey(BathroomType, on_delete=models.CASCADE, null=True)
    apartment_condition = models.ForeignKey(ApartmentCondition, on_delete=models.CASCADE, null=True)
    images = models.ManyToManyField(Image, null=True)
    favorites = models.ManyToManyField(User, related_name="listing_favorites", null=True)
    publication_date = models.DateTimeField(null=True)
    source_publication_date = models.DateTimeField(null=True)
    phone_number = models.CharField(max_length=200, null=True)
    view_count = models.IntegerField(null=True)
    is_published = models.BooleanField(default=False, null=True)
    without_commission = models.BooleanField(default=False, null=True)
    verified = models.BooleanField(default=False, null=True)
    district = models.ForeignKey(Districts, on_delete=models.CASCADE, null=True)
    micro_district = models.ForeignKey(MicroDistricts, on_delete=models.CASCADE, null=True)
    street = models.ForeignKey(Streets, on_delete=models.CASCADE, null=True)
    layout = models.ForeignKey(Layout, on_delete=models.CASCADE, null=True)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="listing_publisher")
    location = models.PointField(geography=True, null=True, srid=4326)

    class Meta:
        db_table = "listing"


# [many to many - Django - Cascade deletion in ManyToManyRelation - Stack Overflow](
# https://stackoverflow.com/questions/3937194/django-cascade-deletion-in-manytomanyrelation)

@receiver(pre_delete, sender=Listing)
def pre_delete_story(sender, instance, **kwargs):
    for image in instance.images.all():
        if image.entries.count() == 1 and instance in image.entries.all():
            # instance is the only Entry authored by this Author, so delete it
            image.delete()


class NumberInFilter(BaseInFilter, NumberFilter):
    pass


class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    min_area = filters.NumberFilter(field_name="total_area", lookup_expr='gte')
    max_area = filters.NumberFilter(field_name="total_area", lookup_expr='lte')
    rooms_count = NumberInFilter(field_name="rooms_count", lookup_expr='in')
    district = ModelChoiceFilter(queryset=Districts.objects.all())

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
