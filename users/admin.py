from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('bio',)}),
    )
    list_display = ['username', 'email', 'is_staff', 'is_active']


admin.site.register(CustomUser, CustomUserAdmin)