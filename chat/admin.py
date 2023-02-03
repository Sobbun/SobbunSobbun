from django.contrib import admin
from .models import ChatRoom, ChatMessage, ChatMessageHistory

# Register your models here.

@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    fields = ('participants ', 'topic', 'updated_at', 'created_at')


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    fields = ('room', 'content', 'author', 'created_at')

@admin.register(ChatMessageHistory)
class ChatMessageHistoryAdmin(admin.ModelAdmin):
    fields = ('message', 'content', 'created_at')