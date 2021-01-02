from realestate.layout.serializers import LayoutSerializer
from django_filters import rest_framework as filters
from rest_framework import viewsets, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_extensions.decorators import paginate
from rest_framework_gis.filters import InBBoxFilter
from drf_multiple_model.viewsets import ObjectMultipleModelAPIViewSet
from drf_multiple_model.pagination import MultipleModelLimitOffsetPagination

from .models import Listing, ProductFilter
from realestate.heating_type.models import HeatingType
from realestate.house_types.models import HouseType
from realestate.heating_type.serializers import HeatingTypeSerializer
from realestate.house_types.serializers import HouseTypeSerializer
from .serializers import ListingSerializer
from ..layout.models import Layout



class StandardResultsSetPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'results': data
        })


class LimitPagination(MultipleModelLimitOffsetPagination):
    default_limit = 100


class ListingsSelectsView(ObjectMultipleModelAPIViewSet):
    querylist = [
        {'queryset': HouseType.objects.all(), 'serializer_class': HouseTypeSerializer},
        {'queryset': HeatingType.objects.all(), 'serializer_class': HeatingTypeSerializer},
         {'queryset': Layout.objects.all(), 'serializer_class': LayoutSerializer},
    ]
    permission_classes = (AllowAny,)
    pagination_class = LimitPagination


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
    filter_backends = (filters.DjangoFilterBackend, InBBoxFilter)
    filterset_fields = ('price', 'is_published', 'rooms_count', 'location')
    filterset_class = ProductFilter
    bbox_filter_field = 'location'
    permission_classes = (AllowAny,)
    bbox_filter_include_overlapping = True  # Optional
