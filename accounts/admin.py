from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display  = ('username', 'email', 'role', 'is_staff', 'date_joined')
    list_filter   = ('role', 'is_staff')
    fieldsets     = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('role', 'avatar', 'bio')}),
    )
