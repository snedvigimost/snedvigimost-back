from django.db import models


class Image(models.Model):
    photo = models.ImageField(upload_to='photos', null=True, max_length=300)

    def __str__(self):
        return self.photo.name
