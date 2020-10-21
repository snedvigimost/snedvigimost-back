from django.contrib import admin
from django.contrib.admin import ModelAdmin

from realestate.countries.models import Country


@admin.register(Country)
class CountryAdmin(ModelAdmin):
    pass

