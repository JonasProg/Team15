from math import pi


def area_circle(r):
    '''Area of circle.

    Calculate the area of a circle based on the radius.

    Args:
        r (float): radius of circle

    Returns:
        float: area of circle
    '''
    if r < 0:
        raise ValueError("The radius must be >= 0.")
    return pi * r**2


def area_square(length):
    """Calculates the area of a square.

    Calculates the area of a square based on the lenth of side.

    Args:
        length (float) : length is the length of side of a square.

    Returns:
        float: area of a square.
    """
    if length < 0:
        raise ValueError("The length of side must be >= 0.")
    area_output = length**2
    return area_output
