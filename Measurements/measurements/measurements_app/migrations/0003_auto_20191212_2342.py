# Generated by Django 2.2.4 on 2019-12-13 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurements_app', '0002_measurement_sensor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='sensor',
            field=models.CharField(max_length=50),
        ),
    ]
