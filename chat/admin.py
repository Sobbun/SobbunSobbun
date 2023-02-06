from django.contrib import admin
from .models import ChatRoom, ChatMessage, ChatMessageHistory

# Register your models here.

@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    fields = ('participants', 'topic_type', 'topic_id', 'topic_text',)


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    fields = ('room', 'content', 'author',)

@admin.register(ChatMessageHistory)
class ChatMessageHistoryAdmin(admin.ModelAdmin):
    fields = ('message', 'content',)