def round_up_to_decimal(value, precision: float = 0.5):
    """
    Helper function to round a given value to a specific precision, for example *.5
    So 5.4 will be rounded to 5.5, 0.9 to 1
    :param value:
    :param precision:
    :return:
    """
    return round(precision * round(float(value) / precision), 1)
