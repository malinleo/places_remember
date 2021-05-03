from django.test import TestCase
from django.urls import reverse
from datetime import date
from io import BytesIO
from accounts.models import User
from ..models import Memory
from social_django.models import UserSocialAuth


class RenderMemoriesViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(id=1, username='username', first_name='first_name',
                                   last_name='last_name', email='email.test@mail.ru')
        user.set_password('PassWord12345.')
        user.save()
        user_social = UserSocialAuth.objects.create(provider='facebook', uid='1961501617337366',
                                                    extra_data={"auth_time": 1619667038, "id": "1961501617337366",
                                                                "expires": 5183998,
                                                                "granted_scopes": ["user_link", "email",
                                                                                   "public_profile"],
                                                                "denied_scopes": None,
                                                                "access_token": "EAAFDYWrKDnoBAMDjDEYVxMSqcUDJQb0Sfh8TLt5xZCWMygigPNL9L4Gznook1CZAFC5a8p5JT7nHoLZAy5fjWZCo6F0l6DbmVm7oNDLCyHw5ALIkQOtZAvdknWRIg6wNoa9av4gLuZCO82Xxp6MsOp4bsPoGjLA2bmUNtJFRCZAOwZDZD",
                                                                "token_type": None,
                                                                "name": "\u041b\u0435\u043e\u043d\u0438\u0434 \u041c\u0430\u043b\u0438\u043d",
                                                                "email": "mr.malin@list.ru",
                                                                "picture": {
                                                                    "data": {"height": 200, "is_silhouette": False,
                                                                             "url": "https://platform-lookaside.fbsbx.com/platform/profilepic/?asid=1961501617337366&height=200&width=200&ext=1622259036&hash=AeRfl3a0cpyPRx0BFug",
                                                                             "width": 200}},
                                                                "profile_url": "https://www.facebook.com/app_scoped_user_id/YXNpZADpBWEZArRTZAaZAVBtRWdWQUpDZAnVUTFpYMWg5ZAjg4b1pQeEtEWWxuRGdZAbGp2SEdQbVlFS18tMjJ2Qm8xRkppYm9ySTFVQkFoczZABc051a1lZAaEYyR0VteEdqUEVWb0NkOTRzelBoUmtIWS14RHMzWENa/"},
                                                    user_id=1)
        user_social.save()

    def test_redirect_if_not_logged_in(self):
        resp = self.client.get('/memories/')
        self.assertRedirects(resp, '/user/social-auth/login/facebook/?next=/memories/', fetch_redirect_response=False)

    def test_view_url_exists_at_desired_location(self):
        self.client.login(username='username', password='PassWord12345.')
        resp = self.client.get(reverse('memories'))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(str(resp.context['user'].username), 'username')

    def test_view_uses_correct_template(self):
        self.client.login(username='username', password='PassWord12345.')
        resp = self.client.get(reverse('memories'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'memories/memories.html')

    def test_only_user_memories_in_list(self):
        self.client.login(username='username', password='PassWord12345.')
        resp = self.client.get(reverse('memories'))
        self.assertEqual(str(resp.context['user'].username), 'username')
        self.assertEqual(resp.status_code, 200)

        self.assertTrue('memories' in resp.context)
        for memory in resp.context['memories']:
            self.assertEqual(resp.context['user'], memory.user)


class AddMemoryTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(id=1, username='username', first_name='first_name',
                                   last_name='last_name', email='email.test@mail.ru')
        user.set_password('PassWord12345.')
        user.save()
        user_social = UserSocialAuth.objects.create(provider='facebook', uid='1961501617337366',
                                                    extra_data={"auth_time": 1619667038, "id": "1961501617337366",
                                                                "expires": 5183998,
                                                                "granted_scopes": ["user_link", "email",
                                                                                   "public_profile"],
                                                                "denied_scopes": None,
                                                                "access_token": "EAAFDYWrKDnoBAMDjDEYVxMSqcUDJQb0Sfh8TLt5xZCWMygigPNL9L4Gznook1CZAFC5a8p5JT7nHoLZAy5fjWZCo6F0l6DbmVm7oNDLCyHw5ALIkQOtZAvdknWRIg6wNoa9av4gLuZCO82Xxp6MsOp4bsPoGjLA2bmUNtJFRCZAOwZDZD",
                                                                "token_type": None,
                                                                "name": "\u041b\u0435\u043e\u043d\u0438\u0434 \u041c\u0430\u043b\u0438\u043d",
                                                                "email": "mr.malin@list.ru",
                                                                "picture": {
                                                                    "data": {"height": 200, "is_silhouette": False,
                                                                             "url": "https://platform-lookaside.fbsbx.com/platform/profilepic/?asid=1961501617337366&height=200&width=200&ext=1622259036&hash=AeRfl3a0cpyPRx0BFug",
                                                                             "width": 200}},
                                                                "profile_url": "https://www.facebook.com/app_scoped_user_id/YXNpZADpBWEZArRTZAaZAVBtRWdWQUpDZAnVUTFpYMWg5ZAjg4b1pQeEtEWWxuRGdZAbGp2SEdQbVlFS18tMjJ2Qm8xRkppYm9ySTFVQkFoczZABc051a1lZAaEYyR0VteEdqUEVWb0NkOTRzelBoUmtIWS14RHMzWENa/"},
                                                    user_id=1)
        user_social.save()

    def test_add_memory_is_correct(self):
        self.client.login(username='username', password='PassWord12345.')
        resp = self.client.post(reverse('add_memory'), {'title': 'title',
                                                        'description': 'description',
                                                        'date': date.today(),
                                                        'address': 'address',
                                                        'location': '56.00637898153531,92.86683082580566'})
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('memories'))


class ChangeMemoryViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(id=1, username='username', first_name='first_name',
                                   last_name='last_name', email='email.test@mail.ru')
        user.set_password('PassWord12345.')
        user.save()
        user_social = UserSocialAuth.objects.create(provider='facebook', uid='1961501617337366',
                                                    extra_data={"auth_time": 1619667038, "id": "1961501617337366",
                                                                "expires": 5183998,
                                                                "granted_scopes": ["user_link", "email",
                                                                                   "public_profile"],
                                                                "denied_scopes": None,
                                                                "access_token": "EAAFDYWrKDnoBAMDjDEYVxMSqcUDJQb0Sfh8TLt5xZCWMygigPNL9L4Gznook1CZAFC5a8p5JT7nHoLZAy5fjWZCo6F0l6DbmVm7oNDLCyHw5ALIkQOtZAvdknWRIg6wNoa9av4gLuZCO82Xxp6MsOp4bsPoGjLA2bmUNtJFRCZAOwZDZD",
                                                                "token_type": None,
                                                                "name": "\u041b\u0435\u043e\u043d\u0438\u0434 \u041c\u0430\u043b\u0438\u043d",
                                                                "email": "mr.malin@list.ru",
                                                                "picture": {
                                                                    "data": {"height": 200, "is_silhouette": False,
                                                                             "url": "https://platform-lookaside.fbsbx.com/platform/profilepic/?asid=1961501617337366&height=200&width=200&ext=1622259036&hash=AeRfl3a0cpyPRx0BFug",
                                                                             "width": 200}},
                                                                "profile_url": "https://www.facebook.com/app_scoped_user_id/YXNpZADpBWEZArRTZAaZAVBtRWdWQUpDZAnVUTFpYMWg5ZAjg4b1pQeEtEWWxuRGdZAbGp2SEdQbVlFS18tMjJ2Qm8xRkppYm9ySTFVQkFoczZABc051a1lZAaEYyR0VteEdqUEVWb0NkOTRzelBoUmtIWS14RHMzWENa/"},
                                                    user_id=1)
        user_social.save()
        Memory.objects.create(user_id=1, title='title', description='description',
                              date=date.today(), address='address', location='56.00637898153531,92.86683082580566')

    def test_change_memory_is_correct(self):
        self.client.login(username='username', password='PassWord12345.')
        cleaned_data = {'title': 'title changed',
                        'description': 'description changed',
                        'date': date.today(),
                        'address': 'address changed',
                        'location': '56.00637898153531,92.86683082580566'}
        resp = self.client.post(reverse('change_memory', kwargs={'pk': 1}), cleaned_data)
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('memories'))
        memory = Memory.objects.get(pk=1)
        memory_cleaned_data = dict()
        for field in memory._meta.fields:
            key = field.__str__().split('.')[-1]
            if key in cleaned_data.keys():
                memory_cleaned_data[key] = field.value_from_object(memory)
        self.assertDictEqual(memory_cleaned_data, cleaned_data)


class DeleteMemoryViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(id=1, username='username', first_name='first_name',
                                   last_name='last_name', email='email.test@mail.ru')
        user.set_password('PassWord12345.')
        user.save()
        user_social = UserSocialAuth.objects.create(provider='facebook', uid='1961501617337366',
                                                    extra_data={"auth_time": 1619667038, "id": "1961501617337366",
                                                                "expires": 5183998,
                                                                "granted_scopes": ["user_link", "email",
                                                                                   "public_profile"],
                                                                "denied_scopes": None,
                                                                "access_token": "EAAFDYWrKDnoBAMDjDEYVxMSqcUDJQb0Sfh8TLt5xZCWMygigPNL9L4Gznook1CZAFC5a8p5JT7nHoLZAy5fjWZCo6F0l6DbmVm7oNDLCyHw5ALIkQOtZAvdknWRIg6wNoa9av4gLuZCO82Xxp6MsOp4bsPoGjLA2bmUNtJFRCZAOwZDZD",
                                                                "token_type": None,
                                                                "name": "\u041b\u0435\u043e\u043d\u0438\u0434 \u041c\u0430\u043b\u0438\u043d",
                                                                "email": "mr.malin@list.ru",
                                                                "picture": {
                                                                    "data": {"height": 200, "is_silhouette": False,
                                                                             "url": "https://platform-lookaside.fbsbx.com/platform/profilepic/?asid=1961501617337366&height=200&width=200&ext=1622259036&hash=AeRfl3a0cpyPRx0BFug",
                                                                             "width": 200}},
                                                                "profile_url": "https://www.facebook.com/app_scoped_user_id/YXNpZADpBWEZArRTZAaZAVBtRWdWQUpDZAnVUTFpYMWg5ZAjg4b1pQeEtEWWxuRGdZAbGp2SEdQbVlFS18tMjJ2Qm8xRkppYm9ySTFVQkFoczZABc051a1lZAaEYyR0VteEdqUEVWb0NkOTRzelBoUmtIWS14RHMzWENa/"},
                                                    user_id=1)
        user_social.save()
        Memory.objects.create(user_id=1, title='title', description='description',
                              date=date.today(), address='address', location='56.00637898153531,92.86683082580566')

    def test_delete_memory_is_correct(self):
        self.client.login(username='username', password='PassWord12345.')
        resp = self.client.post(reverse('delete_memory', kwargs={'pk': 1}))
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('memories'))
        resp = self.client.get('change_memory', kwargs={'pk': 1})
        self.assertEqual(resp.status_code, 404)
