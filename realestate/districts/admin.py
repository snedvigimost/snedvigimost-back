from django.contrib import admin
from django.contrib.admin import ModelAdmin

from realestate.districts.models import Districts


@admin.register(Districts)
class DistrictsAdmin(ModelAdmin):
    pass

