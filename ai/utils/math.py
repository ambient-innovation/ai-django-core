from math import ceil


def round_to_decimal(value, precision: float = 0.5):
    """
    Helper function to round a given value to a specific precision, for example *.5
    So 5.4 will be rounded to 5.5
    :param value:
    :param precision:
    :return:
    """
    return round(precision * round(float(value) / precision), 1)


def round_up_decimal(value, precision: float = 0.5):
    """
    Helper function to round a given value up a specific precision, for example *.5
    So 5.4 will be rounded to 5.5 and 5.6 to 6.0
    :param value:
    :param precision:
    :return:
    """
    return ceil(value * (1 / precision)) / (1 / precision)
