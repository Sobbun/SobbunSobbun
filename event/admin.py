from django.contrib import admin
from .models import Event, EventCategory, EventTag

# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = ('title', 'user', 'description', 'picture', 'status', 'category',  'tags', 'is_deleted')

@admin.register(EventCategory)
class EventCategoryAdmin(admin.ModelAdmin):
    fields = ('name',)

@admin.register(EventTag)
class EventTagAdmin(admin.ModelAdmin):
    fields = ('name',)
