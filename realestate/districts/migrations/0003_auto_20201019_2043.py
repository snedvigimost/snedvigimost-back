# Generated by Django 3.0.6 on 2020-10-19 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0002_auto_20201019_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='districts',
            name='name',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
