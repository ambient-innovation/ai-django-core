# -*- coding: UTF-8 -*-
import re
import sys
from operator import setitem

from django.contrib.humanize.templatetags.humanize import intcomma
from django.template.defaultfilters import floatformat


def numbertotext(value):
    if value == 0:
        return "first"
    elif value == 1:
        return "second"
    else:
        return "third"


def localize_float(value):
    return value.replace('.', ',')


def distinct(l):
    d = {}
    map(setitem, (d,)*len(l), l, [])
    return d.keys()


def float_to_string(value):
    if value is not None:
        return localize_float("%.2f" % value)
    else:
        return "0,00"


def splitString(str):
    result = []

    arr = str.split(',')
    for element in arr:
        element = element.strip()
        if len(element) > 0:
            result.append(element)
    
    return result              
                    

def slugify_file_name(file_name):
    """
        Translit and slugify file name.
    """
    result = ""
    try:
        from django.template.defaultfilters import slugify
        from django.utils.encoding import smart_str
        #print "before: %s" % file_name
        nameext = file_name.rsplit('.',1)
        name = nameext[0] 
        ext = nameext[1]
        #name = name.encode('latin1')
        name = smart_str(slugify(name).replace('-', '_'))
        ext = smart_str(slugify(ext))
        result = '%s.%s' % (name[:40], ext)
        #print "after: %s" % result
    except:
        print "Unexpected error:", sys.exc_info()[0]
    return result


def replace_link_pattern(text):
    text = re.sub(r"(^|[\n ])([\w]+?://[\w]+[^ \"\n\r\t< ]*)", "\g<1><a href=\"\g<2>\" target=\"_blank\">\g<2></a>", text);
    text = re.sub(r"(^|[\n ])((www|ftp)\.[^ \"\t\n\r< ]*)", "\g<1><a href=\"http://\g<2>\" target=\"_blank\">\g<2></a>", text)
    return text


def smart_truncate(text, max_length=100, suffix='...'):
    """Returns a string of at most `max_length` characters, cutting
    only at word-boundaries. If the string was truncated, `suffix`
    will be appended.
    """
    
    if text is None:
        return ''
    
    # Return the string itself if length is smaller or equal to the limit
    if len(text) <= max_length:
        return text
    
    # Cut the string
    value = text[:max_length]
    
    # Break into words and remove the last
    words = value.split(' ')[:-1]
    
    # Join the words and return
    return ' '.join(words) + suffix


def restoreWindows1252Controls(s):
    """Replace C1 control characters in the Unicode string s by the
    characters at the corresponding code points in Windows-1252, where
    possible."""
    import re
    def toWindows1252(match):
        try:
            return chr(ord(match.group(0))).decode('windows-1252')
        except UnicodeDecodeError:
            # No character at the corresponding code point: remove it.
            return ''
    return re.sub(ur'[\u0080-\u0099]', toWindows1252, s)


def number_to_string(value, decimal_digits=0, replacement="-"):
    return intcomma(floatformat(value, decimal_digits)) if value is not None else replacement


def string_or_none_to_string(value, replacement="-"):
    return value if value is not None else replacement
