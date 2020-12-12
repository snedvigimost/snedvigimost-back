from django.db import models


class BathroomType(models.Model):
    title = models.CharField(null=True, max_length=100)

    class Meta:
        db_table = "bathroom_type"

    def __str__(self):
        return self.title
