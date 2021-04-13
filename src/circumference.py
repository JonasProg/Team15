from math import pi


def circ_circle(r):
    '''Circumference of circle.

    Calculate the circumference of a circle based on the radius.

    Args:
        r (float): radius of circle

    Returns:
        float: circumference of circle
    '''
    if r < 0:
        raise ValueError("The radius must be >= 0.")
    return 2 * pi * r


def circ_square(length):
    """Calculates the circumference of a square.

    Calculates the circumference of a square based on the lenth of side.

    Args:
        length (float) : length is the length of side of a square.

    Returns:
        float: circumference of the square.
    """
    if length < 0:
        raise ValueError("The length of side must be >= 0.")
    area_output = 4 * length
    return area_output
