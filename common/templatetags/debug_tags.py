from django.conf import settings
from django import template

register = template.Library()

@register.simple_tag
def show_debug_data():
    return settings.DEBUG and settings.SHOW_DEBUG_DATA