from django.db import models


class HeatingType(models.Model):
    name = models.CharField(null=True, max_length=100)

    class Meta:
        db_table = "heating_type"

    def __str__(self):
        return self.name
