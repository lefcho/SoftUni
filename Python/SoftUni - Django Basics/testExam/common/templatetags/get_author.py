from midExam.utils import get_author_obj
from django import template

register = template.Library()


@register.simple_tag
def get_author():
    return get_author_obj()
