from django.contrib import admin
from django.contrib.admin import ModelAdmin

from realestate.micro_districts.models import MicroDistricts


@admin.register(MicroDistricts)
class MicroDistrictsAdmin(ModelAdmin):
    pass

