from django.shortcuts import render

# Create your views here.
from django_filters import rest_framework as filters
from rest_framework import viewsets

from realestate.micro_districts.models import MicroDistricts, MicroDistrictsFilter
from realestate.micro_districts.serializers import MicroDistrictsSerializer
from realestate.users.permissions import IsUserOrReadOnly


class MicroDistrictsView(viewsets.ModelViewSet):
    model = MicroDistricts
    queryset = MicroDistricts.objects.all()
    serializer_class = MicroDistrictsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('name')
    filterset_class = MicroDistrictsFilter
    permission_classes = (IsUserOrReadOnly,)
