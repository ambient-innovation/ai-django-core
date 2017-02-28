# -*- coding: UTF-8 -*-
from builtins import str


def get_name_by_value(choices_tuple, input_val):
    for val, name in choices_tuple:
        if val == input_val:
            try:
                return str(name)
            except UnicodeDecodeError:
                return name
    return False
