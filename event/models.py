from django.db import models
from common.models import User, Area, AbstractPost, AbstractTag, AbstractCategory

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
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    category = models.ForeignKey(
        EventCategory, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(EventTag)