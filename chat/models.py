from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils.functional import cached_property
from django.contrib.auth import get_user_model

from app.models import SobunPost
from event.models import Event

User = get_user_model()

# Topic의 Choice 리스트
class Topic(models.IntegerChoices):
    TEXT = 1
    USER = 2
    POST_SOBUN = 3
    POST_EVENT = 4

class ChatRoom(models.Model):
    # 채팅 참여자
    participants = models.ManyToManyField(User, related_name='chat_rooms')

    # 채팅시 토픽(상단 공지) 설정할때 사용.
    # topic_type의 Integer 값을 Topic(IntegerChoices)를 이용하여 구분한다
    topic_type = models.IntegerField(choices=Topic.choices)

    # 토픽 텍스트
    topic_text = models.TextField(blank=True)
    # 만약 Type이 2 이상일시, id를 통한 접근을 한다.
    topic_id = models.PositiveIntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @cached_property
    def topic(self):
        match self.topic_type:
            case Topic.TEXT:
                return self.topic_text
            case Topic.USER:
                return User.objects.get(pk=self.topic_id)
            case Topic.POST_SOBUN:
                return SobunPost.objects.get(pk=self.topic_id)
            case Topic.POST_EVENT:
                return Event.objects.get(pk=self.topic_id)
            case _:
                raise AssertionError("Unknown Topic Type")
    

    @cached_property
    def topic_title(self):
        match self.topic_type:
            case Topic.TEXT:
                return self.topic_text
            case Topic.USER:
                return self.topic.profile.nickname
            case Topic.POST_SOBUN | Topic.POST_EVENT:
                return self.topic.title
            case _:
                raise AssertionError("Unknown Topic Type")

    @classmethod
    def set_topic(self, instance):

        # 다른 property 처리는 제대로 된 매칭이 있을시에만.
        def cleanup():
            # 캐시 삭제 시도
            try:
                del self.topic
            except AttributeError:
                pass

            self.topic_id = None
            self.topic_text = ""

        match instance:
            # Text
            case str():
                cleanup()
                self.topic_type = Topic.TEXT
                self.topic_text = instance

            # User
            case User():
                cleanup()
                self.topic_type = Topic.USER
                self.topic_id = instance.id

            # Sobun
            case SobunPost():
                cleanup()
                self.topic_type = Topic.POST_SOBUN
                self.topic_id = instance.id

            # Event
            case Event():
                cleanup()
                self.topic_type = Topic.POST_EVENT
                self.topic_id = instance.id
            
            case _:
                # raise AssertionError("Unknown Topic Type") 
                return False


        return True


    def __str__(self):
        return f'ChatRoom ${self.id}'


# 채팅 메세지
class ChatMessage(models.Model):
    room = models.ForeignKey(
        ChatRoom, on_delete=models.CASCADE, related_name='messages')
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    content = models.TextField()

    checked_by = models.ManyToManyField(User, related_name='checked_messages')
    edited = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ChatMessage #{self.id} in room {self.room_id} by {self.author}"

    @property
    def checked_status(self):
        # should -1 as sender is checked.
        count = self.checked_by.count() - 1
        return 2 if count > 1 else count


class ChatMessageHistory(models.Model):
    message = models.ForeignKey(
        ChatMessage, on_delete=models.CASCADE, related_name='versions')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ChatMessageHistory {self.message.id} in room {self.message.room_id} by {self.message.author} at {self.created_at}"
