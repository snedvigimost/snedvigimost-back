# Generated by Django 3.0.6 on 2020-12-22 13:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0003_news_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='like',
            field=models.ManyToManyField(related_name='news_like', to=settings.AUTH_USER_MODEL),
        ),
    ]