from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    """User Model"""
    username = models.CharField('Username', max_length=50, unique=True)
    password = models.CharField('Password', max_length=100)
    email = models.EmailField('E-mail')
    first_name = models.CharField('First name', max_length=150)
    last_name = models.CharField('Last name', max_length=150)
    user_image = models.ImageField('User image', upload_to='user_photos/', blank=True)
    date_joined = models.DateField('Date joined', auto_now_add=True)
    last_login = models.DateTimeField('Last online', auto_now_add=True, null=True)

    def __str__(self):
        return '%s, %s' % (self.username, self.first_name)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'



