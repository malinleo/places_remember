# Generated by Django 3.2 on 2021-04-23 09:55

from django.db import migrations
import django_google_maps.fields


class Migration(migrations.Migration):

    dependencies = [
        ('places_remember_app', '0004_alter_memory_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memory',
            name='location',
            field=django_google_maps.fields.GeoLocationField(max_length=100, verbose_name='Location'),
        ),
    ]
