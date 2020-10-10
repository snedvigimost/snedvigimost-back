from django_filters import rest_framework as filters
from rest_framework import viewsets, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework_extensions.decorators import paginate

from .models import Listing, ProductFilter
from .serializers import ListingSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 100


@paginate(pagination_class=StandardResultsSetPagination, ordering='-created_at')
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
    filterset_fields = ('price', 'is_published')
    filterset_class = ProductFilter
    permission_classes = (AllowAny,)
