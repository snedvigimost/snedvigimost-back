from django.contrib import admin
from django.contrib.admin import ModelAdmin

from realestate.news.models import News


@admin.register(News)
class NewsAdmin(ModelAdmin):
    pass

