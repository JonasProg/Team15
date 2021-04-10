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
    return pi*r

def circ_square(l):
    """Calculates the circumference of a square.

    Extended description of function.

    Args:
        l (float) : l is the lengths of side of a square.

    Returns:
        float: circumference of the square.
    """
    if l < 0:
        raise ValueError("The length of side must be >= 0.")
    area_output= 4 * l
    return area_output