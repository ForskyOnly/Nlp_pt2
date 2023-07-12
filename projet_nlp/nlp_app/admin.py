from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'first_name', 'last_name', 'is_psychologue', 'is_patient']

admin.site.register(User, CustomUserAdmin)
