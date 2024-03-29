# Generated by Django 3.0.6 on 2020-12-19 12:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('listings', '0031_listing_publisher'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='like',
            field=models.ManyToManyField(related_name='listing_like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='listing',
            name='publisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listing_publisher', to=settings.AUTH_USER_MODEL),
        ),
    ]
