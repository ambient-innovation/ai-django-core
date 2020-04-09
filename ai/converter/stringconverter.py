import os
import re
from builtins import str

from django.contrib.humanize.templatetags.humanize import intcomma
from django.template.defaultfilters import floatformat

from ai.converter.dateconverter import datetime_format


def number_to_text(value):
    if value == 0:
        return "first"
    elif value == 1:
        return "second"
    else:
        return "third"


def distinct(not_distinct_list: list):
    """
    Returns a list with no duplicate elements
    """
    return list(set(not_distinct_list))


def slugify_file_name(file_name, length=40):
    """
    Translit and slugify file name.
    """
    from django.template.defaultfilters import slugify
    from django.utils.encoding import smart_str
    name, ext = os.path.splitext(file_name)
    name = smart_str(slugify(name).replace('-', '_'))
    ext = smart_str(slugify(ext))
    result = '%s%s%s' % (name[:length], "." if ext else "", ext)
    return result


def replace_link_pattern(text):
    text = re.sub(r"(^|[\n ])([\w]+?://[\w]+[^ \"\n\r\t< ]*)",
                  r"\g<1><a href=\"\g<2>\" target=\"_blank\">\g<2></a>", text)
    text = re.sub(r"(^|[\n ])((www|ftp)\.[^ \"\t\n\r< ]*)",
                  r"\g<1><a href=\"http://\g<2>\" target=\"_blank\">\g<2></a>", text)
    return text


def smart_truncate(text, max_length=100, suffix='...'):
    """
    Returns a string of at most `max_length` characters, cutting
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


def restore_windows1252controls(s):
    """
    Replace C1 control characters in the Unicode string s by the
    characters at the corresponding code points in Windows-1252, where
    possible.
    """
    def to_windows1252(match):
        try:
            return chr(ord(match.group(0))).decode('windows-1252')
        except UnicodeDecodeError:
            # No character at the corresponding code point: remove it.
            return ''
    pattern = r'[\u0080-\u0099]'
    try:
        pattern = pattern.decode('raw_unicode_escape')
    except AttributeError:
        # Python 3
        # PEP 414: ur'...' prefix replaced wit just r'...'
        pass
    return re.sub(pattern, to_windows1252, s)


def float_to_string(value, replacement="0,00"):
    def localize_float(value):
        return value.replace('.', ',')
    return localize_float("%.2f" % value) if value is not None else replacement


def date_to_string(value, replacement="-", format="%d.%m.%Y"):
    return value.strftime(format) if value is not None else replacement


def datetime_to_string(value, replacement="-", format="%d.%m.%Y %H:%M"):
    return datetime_format(value, format) if value is not None else replacement


def number_to_string(value, decimal_digits=0, replacement="-"):
    return intcomma(floatformat(value, decimal_digits)) if value is not None else replacement


def string_or_none_to_string(value, replacement="-"):
    return value if value is not None else replacement


def encode_to_xml(text):
    text_str = str(text)
    text_str = text_str.replace('&', '&amp;')
    text_str = text_str.replace('<', '&lt;')
    text_str = text_str.replace('>', '&gt;')

    return text_str
