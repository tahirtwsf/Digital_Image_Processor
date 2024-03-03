import math
def area_of_disk(radius: float) -> float :
    """Returns the area of a circle with a non-negative radius."
    Precondition: radius >= 0
    
    >>> area_of_disk(5)
    78.53981633974483
    >>> area_of_disk(10)
    314.1592653589793
    >>> area_of_disk(15)
    706.8583470577034
    """
    return math.pi * radius ** 2

def distance(x1: float,y1: float,x2: float,y2: float) -> float:  
     """This function returns the distance between two points, 
     given by the coordinates (x1, y1) and (x2, y2).
     
     >>> distance(1.0,2.0,4.0,5.0)
     4.242640687119285
     >>> distance(12.0,13.0,26.0,57.0)
     46.17358552246078
     >>> distance(-4.0,-3.0,50.0,60.0)
     82.97590011563598
     """
     return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
 
def area_of_circle(x1: float,y1: float,x2: float,y2: float) -> float:
    """This function takes two points: the center of a circle, (x1,y1), 
    and a point on the perimeter (x2,y2) and returns the area of a circle.
    The function parameters are the x and y values.
    
    >>>area_of_circle(1.0,2.0,4.0,5.0)
    56.54866776461626
    >>>area_of_circle(5.1,7.2,14.3,21.0)
    864.1893071494802
    >>>area_of_circle(0,0,90.0,1.0)
    25450.04208673091
    """
    return math.pi * distance(x1,y1,x2,y2) ** 2



 
 
 
     

    