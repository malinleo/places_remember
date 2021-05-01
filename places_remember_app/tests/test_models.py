from django.test import TestCase
from datetime import date
from accounts.models import User
from ..models import Memory


class PlacesRememberAppModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(id=1, username='username', password='PassWord12345.', first_name='first_name',
                            last_name='last_name', email='email.test@mail.ru')
        Memory.objects.create(user_id=1, title='title', description='description', date=date.today(), address='address',
                              location='56.00637898153531,92.86683082580566')

    def test_title_label(self):
        memory = Memory.objects.get(id=1)
        title_label = memory._meta.get_field('title').verbose_name
        self.assertEquals(title_label, 'Title')

    def test_description_label(self):
        memory = Memory.objects.get(id=1)
        description_label = memory._meta.get_field('description').verbose_name
        self.assertEquals(description_label, 'Description')

    def test_date_label(self):
        memory = Memory.objects.get(id=1)
        date_label = memory._meta.get_field('date').verbose_name
        self.assertEquals(date_label, 'Date')

    def test_address_label(self):
        memory = Memory.objects.get(id=1)
        address_label = memory._meta.get_field('address').verbose_name
        self.assertEquals(address_label, 'Address')
