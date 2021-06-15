from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _

# Register your models here.

class UserAdminConfig(UserAdmin):
    ordering=('-date',)
    fieldsets=(
        (None, {'fields': ('password',)}),
        (_('Personal info'), {'fields': ('fullname', 'email','avatar','introduction')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Important dates'), {'fields': ('last_login','date')}),
    )
    list_display=('email','fullname','is_staff')

admin.site.register(User,UserAdminConfig)

