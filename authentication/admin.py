from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):

    list_display = ('username', 'domain_name', 'domain_url', 'is_staff', 'is_active')
    search_fields = ('username', 'domain_name', 'domain_url')
    list_filter = ('is_staff', 'is_active')
    

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('domain_name', 'domain_url')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'domain_name', 'domain_url', 'is_staff', 'is_active', 'groups', 'user_permissions'),
        }),
    )

    # Add filter_horizontal for groups and user_permissions
    
filter_horizontal = ('groups', 'user_permissions')
admin.site.register(CustomUser, CustomUserAdmin)
