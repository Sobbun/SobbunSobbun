from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User, Profile, Area, Event, LocationVerification, TrustLevel,  EventCategory, EventTag

# Register your models here.

@admin.register(User)
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

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fields = ('user', 'bio', 'nickname', 'picture')


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    fields = ('code', 'name', 'center', 'version')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = ('title', 'user', 'description', 'picture', 'status', 'category',  'tags', 'is_deleted')

@admin.register(EventCategory)
class EventCategoryAdmin(admin.ModelAdmin):
    fields = ('name',)

@admin.register(EventTag)
class EventTagAdmin(admin.ModelAdmin):
    fields = ('name',)

@admin.register(LocationVerification)
class LocationVerificationAdmin(admin.ModelAdmin):
    fields = ('user', 'area',)

@admin.register(TrustLevel)
class TrustLevelAdmin(admin.ModelAdmin):
    fields = ('user', 'level',)
