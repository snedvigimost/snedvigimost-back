from rest_framework import viewsets

from realestate.house_types.models import HouseType
from realestate.house_types.serializers import HouseTypeSerializer
from realestate.users.permissions import IsUserOrReadOnly


class HouseTypeView(viewsets.ModelViewSet):
    model = HouseType
    queryset = HouseType.objects.all()
    serializer_class = HouseTypeSerializer
    permission_classes = (IsUserOrReadOnly,)
