# Generated by Django 3.0.6 on 2020-12-19 12:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('listings', '0032_auto_20201219_1249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='like',
        ),
        migrations.AddField(
            model_name='listing',
            name='favorites',
            field=models.ManyToManyField(related_name='listing_favorites', to=settings.AUTH_USER_MODEL),
        ),
    ]
