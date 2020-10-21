from django.contrib import admin
from django.contrib.admin import ModelAdmin

from realestate.streets.models import Streets


@admin.register(Streets)
class StreetsAdmin(ModelAdmin):
    pass

