from django.contrib.gis.db import models
from parler.models import TranslatedFields, TranslatableModel

from realestate.countries.models import Country
from realestate.micro_districts.models import MicroDistricts


class Districts(TranslatableModel):
    translations = TranslatedFields(
        any_language=True,
        name=models.CharField(null=True, max_length=250)
    )
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=False)
    micro_districts = models.ManyToManyField(MicroDistricts)
    location = models.PointField(null=True, srid=4326)

    class Meta:
        db_table = "district"

    def __str__(self):
        return self.name
