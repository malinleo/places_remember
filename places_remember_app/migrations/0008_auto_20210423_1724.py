# Generated by Django 3.2 on 2021-04-23 10:24

from django.db import migrations, models
import django_google_maps.fields


class Migration(migrations.Migration):

    dependencies = [
        ('places_remember_app', '0007_auto_20210423_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memory',
            name='address',
            field=django_google_maps.fields.AddressField(max_length=200, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='memory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='memory_photos/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='memory',
            name='location',
            field=django_google_maps.fields.GeoLocationField(max_length=100, null=True, verbose_name='Location'),
        ),
    ]
