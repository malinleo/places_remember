from django.db import models
from django_google_maps import fields as map_fields
from accounts.models import User

# Create your models here.


class Memory(models.Model):
    """ Memory model """
    user = models.ForeignKey(User, verbose_name='Пользователь',
                             on_delete=models.CASCADE, default=-1)
    title = models.CharField('Заголовок', max_length=150)
    description = models.TextField('Описание', max_length=5000)
    location = map_fields.GeoLocationField('Геолокация', max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Воспоминание'
        verbose_name_plural = 'Воспоминания'
