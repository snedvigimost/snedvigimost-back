from django.contrib import admin
from django.contrib.admin import ModelAdmin

from realestate.listings.models import Listing


@admin.register(Listing)
class ListingAdmin(ModelAdmin):
    pass
