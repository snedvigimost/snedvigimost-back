# Generated by Django 3.0.6 on 2021-01-01 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20210101_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image_url',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
