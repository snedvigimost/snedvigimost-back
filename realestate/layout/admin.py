from django.contrib import admin
from django.contrib.admin import ModelAdmin

from realestate.layout.models import Layout


@admin.register(Layout)
class MicroDistrictsAdmin(ModelAdmin):
    pass

