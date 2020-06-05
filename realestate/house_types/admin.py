from django.contrib import admin
from django.contrib.admin import ModelAdmin

from realestate.house_types.models import HouseType


@admin.register(HouseType)
class HouseTypeAdmin(ModelAdmin):
    pass

