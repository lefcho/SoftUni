from django import template

from examPrep1.utils import get_user_obj

register = template.Library()


@register.simple_tag
def get_user():
    return get_user_obj()