# coding=utf-8
from django import template

register = template.Library()

@register.filter(name='mult')
def mult(value, arg):
    """
    Multiplies the arg and the value

    :param value:
    :param arg:
    :return:
    """
    if value:
        value = "%s" % value
        if type(value) is str and len(value) > 0:
            return float(value.replace(",",".")) * float(arg)

    return None

@register.filter(name='sub')
def sub(value, arg):
    """
    Subtracts the arg from the value

    :param value:
    :param arg:
    :return:
    """
    value = nonetozero(value)
    arg = nonetozero(arg)
    return int(value) - int(arg)


@register.filter(name='div')
def div(value, arg):
    """
    Divides the value by the arg

    :param value:
    :param arg:
    :return:
    """
    if value:
        return float(value) / float(arg)
    else:
        return None


def nonetozero(value):
    """
    Returns 0 if value is None

    :param value:
    :return:
    """
    if value is None:
        return 0
    else:
        return value

@register.filter(name='toint')
def toint(value):
    """
    Parses a string to int value

    :param value:
    :return:
    """
    return int(value)

@register.filter()
def currency(value):
    """
    Converts the number to an €-amount
    """
    if value:
        return (("%.2f" % round(value, 2)) + "€").replace(".", ",")
    else:
        return "-"