from rest_flex_fields import FlexFieldsModelSerializer

from .models import Districts
from ..countries.serializers import CountrySerializer
from ..micro_districts.serializers import MicroDistrictsSerializer


class DistrictsSerializer(FlexFieldsModelSerializer):
    micro_districts = MicroDistrictsSerializer(read_only=True, many=True)

    class Meta:
        model = Districts
        fields = '__all__'
        expandable_fields = {
            'country': CountrySerializer
        }
