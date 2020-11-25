# Create your views here.
from rest_framework import viewsets

from realestate.heating_type.models import HeatingType
from realestate.heating_type.serializers import HeatingTypeSerializer
from realestate.users.permissions import IsUserOrReadOnly


class HeatingTypeView(viewsets.ModelViewSet):
    model = HeatingType
    queryset = HeatingType.objects.all()
    serializer_class = HeatingTypeSerializer
    permission_classes = (IsUserOrReadOnly,)
