from django.db import models


class HouseType(models.Model):
    title = models.CharField(null=True, max_length=100)

    class Meta:
        db_table = "house_type"

    def __str__(self):
        return self.title
