# Generated by Django 3.2 on 2021-04-23 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places_remember_app', '0013_alter_memory_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memory',
            name='image',
            field=models.ImageField(blank=True, default='/media/default.jpg', null=True, upload_to='memory_photos/', verbose_name='Image'),
        ),
    ]
