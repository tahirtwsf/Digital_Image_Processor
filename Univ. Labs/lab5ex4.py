import math
def height(length: float, angle: float) -> float:
    """This function takes the length of a ladder, measured in metres, 
    angle that it forms with the ground as it leans against the wall, measured
    in degrees. It returns the height reached by the ladder. 
    Preconditions:
    length of ladder > 0
    0 =< angle =< 90 (The function will still work if the angle is greater than 90.
                      However, it is specified that the angle is the one which the 
                      ladder forms with the ground as it leans against the wall.)
    >>>height(5.0, 45.0)
    3.5355339059327378 
    >>>height(10.0,90.0)
    10.0
    >>>height(100.4, 43.7)
    69.36459407211659
    """
    return length * math.sin(math.radians(angle))