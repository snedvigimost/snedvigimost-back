from django_filters import rest_framework as filters
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from .models import Listing, ProductFilter
from .serializers import CreateListingSerializer, ListingSerializer
from ..users.permissions import IsUserOrReadOnly


class ListingViewSet(mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    """
    Updates and retrieves user accounts
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('price',)
    filterset_class = ProductFilter
    permission_classes = (IsUserOrReadOnly,)


class ListingCreateViewSet(mixins.CreateModelMixin,
                           viewsets.GenericViewSet):
    """
    Creates user accounts
    """
    queryset = Listing.objects.all()
    serializer_class = CreateListingSerializer
    permission_classes = (AllowAny,)
