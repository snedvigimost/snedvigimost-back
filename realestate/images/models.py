from django.db import models


class Image(models.Model):
  photo = models.FileField(upload_to='photos', null=True)
