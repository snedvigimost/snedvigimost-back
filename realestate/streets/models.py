from django.db import models
from django.db.models import CharField, ForeignKey, Model
from django_filters import rest_framework as filters

from realestate.districts.models import Districts


class Streets(Model):
    name = CharField(null=True, max_length=250)
    district = ForeignKey(Districts, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name


class StreetFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr='contains')

    class Meta:
        model = Streets
        fields = ['name']
