from django.db import models
from django.contrib.auth import get_user_model
from common.models import Area, AbstractPost, AbstractTag, AbstractCategory

User = get_user_model()

# Create your models here.
class EventCategory(AbstractCategory):
    pass


class EventTag(AbstractTag):
    pass


class Event(AbstractPost):
    user = models.ForeignKey(
        User, null=True, related_name='event_posts', on_delete=models.SET_NULL)
    area = models.ForeignKey(Area, null=True, on_delete=models.SET_NULL)

    status = models.CharField(max_length=20, blank=True)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)

    category = models.ForeignKey(
        EventCategory, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(EventTag)