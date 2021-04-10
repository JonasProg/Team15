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
    return