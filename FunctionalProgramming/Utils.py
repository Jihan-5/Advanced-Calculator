def validate_input(value):
    """ Validate if input is a number """
    try:
        float(value)
        return True
    except ValueError:
        return False
