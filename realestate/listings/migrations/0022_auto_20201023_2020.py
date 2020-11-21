# Generated by Django 3.0.6 on 2020-10-23 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('streets', '0001_initial'),
        ('micro_districts', '0002_remove_microdistricts_district'),
        ('listings', '0021_listing_layout'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='micro_district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='micro_districts.MicroDistricts'),
        ),
        migrations.AddField(
            model_name='listing',
            name='street',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='streets.Streets'),
        ),
    ]