# Generated by Django 3.0.6 on 2020-11-29 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0006_auto_20201125_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='districts',
            name='name_en',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='districts',
            name='name_ru',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='districts',
            name='name_uk',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
