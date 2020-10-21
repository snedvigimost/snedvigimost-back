from rest_flex_fields import FlexFieldsModelSerializer

from .models import Streets
from ..districts.serializers import DistrictsSerializer


class StreetsSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Streets
        fields = '__all__'
        expandable_fields = {
             'district': DistrictsSerializer
        }
