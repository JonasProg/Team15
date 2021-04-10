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
    return pi*r**2

def area_square(l):
    return True