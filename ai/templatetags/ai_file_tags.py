# coding=utf-8
from django import template
import os
from django.conf import settings

register = template.Library()



@register.filter
def filename(value):
    """
    Shortens the filename to maxlength 25 without loosing the file extension

    :param file:
    :return filename with a max length of 25
    """
    MAX_LENGTH = 25
    name = os.path.basename(value.url)
    if len(name) > MAX_LENGTH:
        ext = name.split('.')[-1]
        name = u"%s[..].%s" % (name[:MAX_LENGTH], ext)
    return name


@register.filter
def filesize(value):
    """
    Returns the filesize of the filename given in value

    :param value:
    :return filesize:
    """
    try:
        return os.path.getsize("%s%s" % (settings.MEDIA_ROOT, value))
    except:
        return 0