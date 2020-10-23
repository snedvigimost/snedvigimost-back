from django.db import models
from django.db.models import CharField, Model
from django_filters import rest_framework as filters


class MicroDistricts(Model):
    name = CharField(null=True, max_length=250)

    def __str__(self):
        return self.name


class MicroDistrictsFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr='contains')

    class Meta:
        model = MicroDistricts
        fields = ['name']
