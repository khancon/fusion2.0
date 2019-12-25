# users/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username','phonenumber','first_name','last_name']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Platform)
admin.site.register(Playlist)
admin.site.register(Song)


