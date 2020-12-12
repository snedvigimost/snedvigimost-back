from rest_framework import viewsets

from realestate.apartment_condition.models import ApartmentCondition
from realestate.apartment_condition.serializers import ApartmentConditionSerializer
from realestate.users.permissions import IsUserOrReadOnly


class ApartmentConditionView(viewsets.ModelViewSet):
    model = ApartmentCondition
    queryset = ApartmentCondition.objects.all()
    serializer_class = ApartmentConditionSerializer
    permission_classes = (IsUserOrReadOnly,)
