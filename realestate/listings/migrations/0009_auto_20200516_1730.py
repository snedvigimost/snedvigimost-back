# Generated by Django 3.0.6 on 2020-05-16 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_auto_20200516_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='floor',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='floor_in_house',
            field=models.IntegerField(null=True),
        ),
    ]
