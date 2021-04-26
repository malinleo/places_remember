from django.db import models
from location_field.models.plain import PlainLocationField
from accounts.models import User
from datetime import date

# Create your models here.


class Memory(models.Model):
    """ Memory model """
    user = models.ForeignKey(User, verbose_name='User',
                             on_delete=models.CASCADE, default=-1)
    title = models.CharField('Title', max_length=100)
    description = models.TextField('Description', max_length=5000)
    date = models.DateField('Date', default=date.today)
    address = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['address'], zoom=7, default='')
    image = models.ImageField('Image', upload_to='memory_photos/', blank=True, null=True, default='default.jpg')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Memory'
        verbose_name_plural = 'Memories'
