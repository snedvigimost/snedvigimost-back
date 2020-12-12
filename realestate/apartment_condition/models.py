from django.db import models


class ApartmentCondition(models.Model):
    title = models.CharField(null=True, max_length=100)

    class Meta:
        db_table = "apartment_condition"

    def __str__(self):
        return self.title
