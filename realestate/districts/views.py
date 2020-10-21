from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from realestate.districts.models import Districts
from realestate.districts.serializers import DistrictsSerializer
from realestate.users.permissions import IsUserOrReadOnly


class DistrictsView(viewsets.ModelViewSet):
    model = Districts
    queryset = Districts.objects.all()
    serializer_class = DistrictsSerializer
    permission_classes = (IsUserOrReadOnly,)
