from rest_flex_fields import FlexFieldsModelSerializer

from .models import Districts
from ..countries.serializers import CountrySerializer


class DistrictsSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Districts
        fields = '__all__'
        expandable_fields = {
            'country': CountrySerializer
        }
