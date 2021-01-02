from realestate.users.models import User
from django.db.models import CharField, Model
from django.db import models


class Comment(Model):
    body = models.TextField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "comment"

    def __str__(self):
        return self.title
