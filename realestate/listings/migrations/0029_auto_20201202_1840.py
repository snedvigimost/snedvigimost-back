# Generated by Django 3.0.6 on 2020-12-02 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bathroom_type', '0001_initial'),
        ('listings', '0028_auto_20201125_2329'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='bathroom_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bathroom_type.BathroomType'),
        ),
        migrations.AddField(
            model_name='listing',
            name='without_commission',
            field=models.BooleanField(default=False, null=True),
        ),
    ]