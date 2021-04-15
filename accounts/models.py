from django.db import models
from django.contrib.auth.models import AbstractUser
from django_google_maps import fields as map_fields

# Create your models here.


class User(AbstractUser):
    """User Model"""
    username = models.CharField('Имя пользователя', max_length=50, unique=True)
    password = models.CharField('Пароль', max_length=100)
    email = models.EmailField('E-mail')
    first_name = models.CharField('Имя', max_length=150)
    last_name = models.CharField('Фамилия', max_length=150)
    user_image = models.ImageField('Изображение', upload_to='user_photos/', blank=True)
    date_joined = models.DateField('Дата регистрации', auto_now_add=True)
    last_login = models.DateTimeField('Заходил последний раз', auto_now_add=True, null=True)
    user_url = models.SlugField('URL пользователя', max_length=160, unique=True)

    def __str__(self):
        return '%s, %s' % (self.username, self.first_name)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


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
