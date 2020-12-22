from django.contrib import admin
from django.contrib.admin import ModelAdmin

from realestate.heating_type.models import HeatingType


@admin.register(HeatingType)
class HeatingTypeAdmin(ModelAdmin):
    pass

