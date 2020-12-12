from django.contrib import admin
from django.contrib.admin import ModelAdmin

from realestate.bathroom_type.models import BathroomType


@admin.register(BathroomType)
class BathroomTypeAdmin(ModelAdmin):
    pass

