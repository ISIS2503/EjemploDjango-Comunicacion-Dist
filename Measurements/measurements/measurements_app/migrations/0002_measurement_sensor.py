# Generated by Django 2.2.4 on 2019-12-13 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurements_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='sensor',
            field=models.IntegerField(default=None),
        ),
    ]
