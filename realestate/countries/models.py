from django.db import models


class Country(models.Model):
    name = models.CharField(null=True, max_length=250)

    class Meta:
        db_table = "country"

    def __str__(self):
        return self.name
