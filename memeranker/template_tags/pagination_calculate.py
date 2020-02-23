from django import template

register = template.Library()

@register.simple_tag
def func():
    return 1