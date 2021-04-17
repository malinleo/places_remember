from django.contrib import admin
from accounts.models import User
from places_remember_app.models import Memory

# Register your models here.

admin.site.register(User)
admin.site.register(Memory)
