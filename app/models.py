from django.db import models
from common.models import User, Area, AbstractPost, AbstractTag, AbstractCategory
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class GoodsCategory(AbstractCategory):
    pass

class SobunTag(AbstractTag):
    pass

class SobunPost(AbstractPost):
    user = models.ForeignKey(
        User, null=True, related_name='sobun_posts', on_delete=models.SET_NULL)
    area = models.ForeignKey(Area, null=True, on_delete=models.SET_NULL)

    product = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    schedule = models.DateTimeField()

    category = models.ForeignKey(GoodsCategory, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(SobunTag)

    sobun_price = models.IntegerField()
    sobun_unit = models.CharField(max_length=30)


class Sobun(models.Model):
    post = models.ForeignKey(SobunPost, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(
        User, related_name='sobuns', on_delete=models.CASCADE)

    time = models.DateTimeField()
    whether = models.BooleanField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [("post", "user")]
        index_together = [("post", "user")]
        verbose_name_plural = "Sobun"

    def __str__(self):
        return f"Sobun from {self.post} to {self.user}"


class SobunRate(models.Model):
    user_from = models.ForeignKey(
        User, related_name='ratings_given', on_delete=models.SET_NULL, null=True)
    user_to = models.ForeignKey(
        User, related_name='ratings_received', on_delete=models.CASCADE)
    sobun = models.ForeignKey(
        Sobun, null=True, on_delete=models.SET_NULL)

    type = models.IntegerField()
    detail = models.TextField(max_length=300)

    created_at = models.DateTimeField(auto_now_add=True)