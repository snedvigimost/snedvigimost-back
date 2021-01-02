# Generated by Django 3.0.6 on 2021-01-01 19:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0004_news_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='like',
            field=models.ManyToManyField(null=True, related_name='news_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
