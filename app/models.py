from django.db import models
from django.contrib.auth.models import AbstractUser
from common.models import User

# Create your models here.
class Area(models.Model):
    code = models.IntegerField()
    name = models.TextField()
    center = models.TextField()
    version = models.DateField()

    def __str__(self):
        return self.name

class Event(models.Model):
    area = models.ForeignKey(Area, null=True, on_delete=models.SET_NULL)

    name = models.TextField(max_length=80)
    description = models.TextField()
    status = models.CharField(max_length=20, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class GoodsCategory(models.Model):
    name = models.TextField()


class LocationVerification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ["user", "area"]

    def __str__(self) -> str:
        return self.user.user.username


class TrustLevel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    level = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.user.username


class SobunPost(models.Model):
    goods_category = models.ForeignKey(
        GoodsCategory, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    area = models.ForeignKey(Area, null=True, on_delete=models.SET_NULL)

    title = models.TextField()
    product = models.TextField()
    description = models.TextField()
    picture = models.TextField()
    place = models.TextField()
    schedule = models.DateTimeField()

    is_deleted = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Sobun(models.Model):
    post = models.ForeignKey(SobunPost, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    time = models.DateTimeField()
    whether = models.BooleanField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ["post", "user"]


class ChatRoom(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    post = models.ForeignKey(SobunPost, null=True, on_delete=models.SET_NULL)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ChatMessage(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    sent_user = models.ForeignKey(User, on_delete=models.CASCADE)
    messages = models.TextField(max_length=1000)
    checked = models.BooleanField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=15, blank=True)
    content = models.TextField()
    picture = models.TextField()

    updated_at = models.DateTimeField(auto_now=True)


class Rate(models.Model):
    user_from = models.ManyToManyField(User, related_name="rating_to")
    user_to = models.ForeignKey(User, on_delete=models.CASCADE)
    sobun_post = models.ForeignKey(
        SobunPost, null=True, on_delete=models.SET_NULL)

    type = models.IntegerField()
    detail = models.TextField(max_length=300)

    created_at = models.DateTimeField(auto_now_add=True)
