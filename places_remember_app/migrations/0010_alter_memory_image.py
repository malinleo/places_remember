# Generated by Django 3.2 on 2021-04-23 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places_remember_app', '0009_auto_20210423_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memory',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='memory_photos/', verbose_name='Image'),
        ),
    ]