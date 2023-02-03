from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model

User = get_user_model()


class ChatRoom(models.Model):
    participants = models.ManyToManyField(User, related_name='chat_rooms')

    topic_type = models.ForeignKey(
        ContentType, on_delete=models.SET_NULL, null=True, blank=True)
    topic_id = models.PositiveIntegerField(null=True, blank=True)
    topic_text = models.TextField(blank=True)
    topic = GenericForeignKey('topic_type', 'topic_id')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ChatMessage(models.Model):
    room = models.ForeignKey(
        ChatRoom, on_delete=models.CASCADE, related_name='messages')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

    checked_by = models.ManyToManyField(User, related_name='checked_messages')
    edited = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ChatMessage {self.id} in room {self.room_id} by {self.author}"

    @property
    def checked_status(self):
        count = self.checked_by.count()
        return 2 if count > 1 else count


class ChatMessageHistory(models.Model):
    message = models.ForeignKey(
        ChatMessage, on_delete=models.CASCADE, related_name='versions')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
