# Generated by Django 3.0.6 on 2021-11-09 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0007_auto_20201125_2129'),
        ('listings', '0036_auto_20211109_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='images',
            field=models.ManyToManyField(null=True, to='images.Image'),
        ),
    ]
