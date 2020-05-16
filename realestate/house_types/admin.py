from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.forms import ModelForm

from realestate.house_types.models import HouseType


from django import forms
from django.contrib.auth.models import User

#
# class ArticleForm(ModelForm):
#     class Meta:
#         model = HouseType
#         fields = ['type']

# class DogRequestForm(forms.Form):
#     id = forms.IntegerField(required=False, widget=forms.HiddenInput())
#     type = forms.ModelChoiceField(queryset=HouseType.objects.all())



@admin.register(HouseType)
class HouseTypeAdmin(ModelAdmin):
    pass

