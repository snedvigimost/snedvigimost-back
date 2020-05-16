from django.db import models


class Image(models.Model):
  photo = models.ImageField(upload_to='photos', null=True)
