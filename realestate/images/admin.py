from django.contrib import admin
from django.contrib.admin import ModelAdmin

from realestate.images.models import Image


@admin.register(Image)
class ImageAdmin(ModelAdmin):
    pass
