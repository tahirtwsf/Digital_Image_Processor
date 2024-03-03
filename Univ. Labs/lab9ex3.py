from math import pi
def make_pi():
    """Takes no arguments, simply returns the first three digits of the number "pi".
    Example:
    >>> make_pi()
    [3, 1, 4]
    """
    x = str(pi)
    return [int(x[0]), int(x[2]), int(x[3])]