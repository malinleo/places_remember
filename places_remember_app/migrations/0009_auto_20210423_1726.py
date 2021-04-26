# Generated by Django 3.2 on 2021-04-23 10:26

from django.db import migrations
import django_google_maps.fields


class Migration(migrations.Migration):

    dependencies = [
        ('places_remember_app', '0008_auto_20210423_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memory',
            name='address',
            field=django_google_maps.fields.AddressField(blank=True, default='', max_length=200, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='memory',
            name='location',
            field=django_google_maps.fields.GeoLocationField(blank=True, max_length=100, null=True, verbose_name='Location'),
        ),
    ]
