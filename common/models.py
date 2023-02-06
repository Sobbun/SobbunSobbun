from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class User(AbstractUser):
    phone = PhoneNumberField(unique=True, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=15, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    picture = models.ImageField(upload_to='pictures/profile', blank=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.__str__()


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
        unique_together = [("user", "area")]
        index_together = [("user", "area")]
        verbose_name_plural = "LocationVerification"

    def __str__(self):
        return f"Location verification of {self.user} to {self.area}"


class TrustLevel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='trust_level')
    level = models.FloatField(default=50, validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}"


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
    picture = models.ImageField(upload_to='pictures/post')

    category = models.ForeignKey(
        AbstractCategory, on_delete=models.SET_NULL, related_name='posts', null=True)
    tags = models.ManyToManyField(AbstractTag, related_name='posts')

    is_deleted = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True

# 생성시 기본 인스턴스
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        TrustLevel.objects.create(user=instance)
    instance.profile.save()
    instance.trust_level.save()