from django.db import models

from realestate.countries.models import Country


class Districts(models.Model):
    name = models.CharField(null=True, max_length=250)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name
