from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name='get_first_char')
def get_first_char(value):
    """
    Returns the first char of the given string
    :param value:
    :return:
    """
    return value[:1]


@register.filter(name='concat')
def concat(obj, str):
    """
    Concats the the two given strings

    :param obj:
    :param str:
    :return:
    """
    return f"{obj}{str}"


@register.filter
@stringfilter
def trim(value):
    """
    Strips the whitespaces of the given value

    :param value:
    :return:
    """
    return value.strip()
