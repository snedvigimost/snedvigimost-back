from rest_framework import viewsets

from realestate.countries.models import Country
from realestate.countries.serializers import CountrySerializer
from realestate.users.permissions import IsUserOrReadOnly


class CountryView(viewsets.ModelViewSet):
    model = Country
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (IsUserOrReadOnly,)
