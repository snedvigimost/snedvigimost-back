from django_filters import rest_framework as filters
from rest_framework import viewsets

from realestate.streets.models import Streets, StreetFilter
from realestate.streets.serializers import StreetsSerializer
from realestate.users.permissions import IsUserOrReadOnly


class StreetsView(viewsets.ModelViewSet):
    model = Streets
    queryset = Streets.objects.all()
    serializer_class = StreetsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('name')
    filterset_class = StreetFilter
    permission_classes = (IsUserOrReadOnly,)
