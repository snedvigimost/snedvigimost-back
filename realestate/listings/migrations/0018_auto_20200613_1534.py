# Generated by Django 3.0.6 on 2020-06-13 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0017_listing_publisher_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='source',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='url',
            field=models.CharField(max_length=200, null=True),
        ),
    ]