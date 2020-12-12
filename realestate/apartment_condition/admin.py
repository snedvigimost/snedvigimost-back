from django.contrib import admin
from django.contrib.admin import ModelAdmin

from realestate.apartment_condition.models import ApartmentCondition


@admin.register(ApartmentCondition)
class ApartmentConditionAdmin(ModelAdmin):
    pass

