def circ_circle(r):
    return

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