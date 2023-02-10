# app/templatetags/urlparams.py
from django import template
from urllib.parse import urlencode
import re

register = template.Library()

@register.filter
def render_image_tag(value, _args = ""):
    if '|' in _args and '=' in _args:
        args = {k: v  for k, v in [i.split('=') for i in _args.split('|')]}
    else:
        args = {'src': _args}

    additional = []
    src = args.get('src', '')
    inline_style = args.get('style', None)
    inline_class = args.get('class', None)

    print(args)

    match src:
        case '[event_static]':
            path = '/static/img/event/'
        case '[static]':
            path = '/static/'
        case _:
            path = src

    if inline_class:
        additional.append(f'class="{inline_class}"')
    if inline_style:
        additional.append(f'style="{inline_style}"')

    return re.sub(r"\[image\s+[\"'](.+?)[\"']\]", fr'<img src="{path}\1" {" ".join(additional)} />', value)

@register.filter
def is_empty_helper(value):
    match value:
        case str():
            return len(value) > 0
        case None:
            return False
        case _:
            return value

@register.filter
def spliter(value, _arg):
    match _arg:
        case '[newline]':
            arg = '\n'
        case _:
            arg = ' '

    l = value.split(arg)
    return [i.strip() for i in l]


@register.filter
def remove_image_tag(value):
    return re.sub(r"\[image\s+[\"'](.+?)[\"']\]", '', value)