from django import template

register = template.Library()

@register.filter(name='mult')
def mult(value, arg):
    "Multiplies the arg and the value"
    if value:
        value = "%s" % value
        if type(value) is str and len(value) > 0:
            return float(value.replace(",",".")) * float(arg)

    return None

@register.filter(name='sub')
def sub(value, arg):
    "Subtracts the arg from the value"
    value = nonetozero(value)
    arg = nonetozero(arg)
    return int(value) - int(arg)


@register.filter(name='div')
def div(value, arg):
    "Divides the value by the arg"
    if value:
        return float(value) / float(arg)
    else:
        return None


def nonetozero(value):
    if value is None:
        return 0
    else:
        return value

@register.filter(name='toint')
def toint(value):
    return int(value)

