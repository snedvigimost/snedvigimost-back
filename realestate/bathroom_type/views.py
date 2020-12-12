from rest_framework import viewsets

from realestate.bathroom_type.models import BathroomType
from realestate.bathroom_type.serializers import BathroomTypeSerializer
from realestate.users.permissions import IsUserOrReadOnly


class BathroomTypeView(viewsets.ModelViewSet):
    model = BathroomType
    queryset = BathroomType.objects.all()
    serializer_class = BathroomTypeSerializer
    permission_classes = (IsUserOrReadOnly,)
