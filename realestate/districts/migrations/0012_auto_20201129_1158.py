# Generated by Django 3.0.6 on 2020-11-29 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0011_auto_20201129_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='districts',
            name='name',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.DeleteModel(
            name='DistrictsTranslation',
        ),
    ]
