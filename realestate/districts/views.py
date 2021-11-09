# Create your views here.
from rest_framework import viewsets, pagination
from rest_framework_extensions.decorators import paginate

from realestate.districts.models import Districts
from realestate.districts.serializers import DistrictsSerializer
from realestate.users.permissions import IsUserOrReadOnly


@paginate(pagination_class=pagination.PageNumberPagination, page_size=50)
class DistrictsView(viewsets.ModelViewSet):
    max_paginate_by = 100
    model = Districts
    queryset = Districts.objects.all()
    serializer_class = DistrictsSerializer
    permission_classes = (IsUserOrReadOnly,)
