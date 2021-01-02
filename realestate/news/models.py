from realestate.taggs.models import Tag
from realestate.comments.models import Comment
from django.db import models

from realestate.users.models import User


class News(models.Model):
    title = models.CharField(null=True, max_length=100)
    subtitle = models.CharField(max_length=500, null=True, blank=False)
    image_url = models.CharField(max_length=500, null=True, blank=False)
    body = models.TextField(null=True)
    slug = models.SlugField(max_length=250, unique=True, null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    like = models.ManyToManyField(User, related_name="news_like", null=True)
    tags = models.ManyToManyField(Tag, related_name="news_tags", null=True)
    comments = models.ManyToManyField(Comment, related_name="news_comment", null=True)

    class Meta:
        db_table = "news"

    def __str__(self):
        return self.title
