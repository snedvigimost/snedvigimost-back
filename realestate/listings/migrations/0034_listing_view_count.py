# Generated by Django 3.0.6 on 2020-12-19 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0033_auto_20201219_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='view_count',
            field=models.IntegerField(null=True),
        ),
    ]
