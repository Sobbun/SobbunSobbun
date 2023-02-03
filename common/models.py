from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class User(AbstractUser):
    phone = PhoneNumberField(unique=True, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=15, blank=True)
    content = models.TextField()
    picture = models.ImageField(upload_to='profile_pictures')

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user


class Area(models.Model):
    code = models.IntegerField()
    name = models.TextField()
    center = models.TextField()
    version = models.DateField()

    def __str__(self):
        return self.name


class Event(models.Model):
    area = models.ForeignKey(Area, null=True, on_delete=models.SET_NULL)

    name = models.CharField(max_length=80)
    description = models.TextField()
    status = models.CharField(max_length=20, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class LocationVerification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ["user", "area"]

    class Meta:
        unique_together = [("user", "area")]
        index_together = [("user", "area")]
        verbose_name_plural = "LocationVerification"

    def __str__(self):
        return f"Location verification of {self.user} to {self.area}"


class TrustLevel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    level = models.FloatField(default=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user


class AbstractCategory(models.Model):
    name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class AbstractTag(models.Model):
    name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class AbstractPost(models.Model):
    user = models.ForeignKey(
        User, null=True, related_name='posts', on_delete=models.SET_NULL)

    title = models.CharField(max_length=100)
    description = models.TextField()
    picture = models.ImageField(upload_to='post_pictures')

    category = models.ForeignKey(
        AbstractCategory, on_delete=models.SET_NULL, related_name='posts', null=True)
    tags = models.ManyToManyField(AbstractTag, related_name='posts')

    is_deleted = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
