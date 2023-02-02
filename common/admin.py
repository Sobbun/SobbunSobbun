from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User

# Register your models here.


class CustomUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + (
        'is_active', 'phone', 'last_login', 'updated_at', 'date_joined'
    )

    fieldsets = UserAdmin.fieldsets + (
        (_("Additional Fields"), {'fields': ('phone',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (_("Additional Fields"), {'fields': ('phone',)}),
    )

    def __init__(self, *args, **kwargs):
        super(UserAdmin, self).__init__(*args, **kwargs)


admin.site.register(User, CustomUserAdmin)
