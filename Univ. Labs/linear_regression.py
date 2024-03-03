"""
ECOR 1051 Fall 2019 Lab 13
"""
from typing import Set, Tuple
# See Practical Programming, Chapter 8, section Type Annotations For Lists,
# and Chapter 11, first paragraph of section Creating New Type Annotations. 

def get_points() -> Set[Tuple[float, float]]:
    """Return a set of (x, y) points.
    
    >>> get_points()
    {(1.0, 5.0), (3.5, 12.5), (2.0, 8.0)}
    # The order of the points may vary, depending on how sets are implemented
    # in the version of Python you're using.
    """
    return {(1.0, 5.0), (2.0, 8.0), (3.5, 12.5)}

def fit_line_to_points(points: Set[Tuple[float, float]]) -> Tuple[float, float]:
    """
    This function is passed a set of tuples, with each tuple representing one
    (x, y) point. The function returns a tuple, which contains the slope and  
    y-intercept of the best-fit straight line through the points.
    
    >>>fit_line_to_points(points = {(1.0, 5.0), (2.0, 8.0), (3.5, 12.5)})
    (3.0, 2.0)
    
    """
    sumx = 0
    sumy = 0
    sumxy = 0
    sumxx = 0 
    n = len(points) 
    for i in points: 
        x, y = i
        sumx += x
        sumy += y
        sumxy += x * y
        sumxx += x**2
    m = (sumx*sumy - n*sumxy) / (sumx**2 - n*sumxx)
    b = (sumx*sumxy - sumxx*sumy) / (sumx**2 - n*sumxx)
    return m, b

def read_points(filename: str) -> Set[Tuple[float, float]]:
    """returns a set of tuples of floats from a given file.
    >>> read_points('data.txt')
    {(1.0, 5.0), (3.5, 12.5), (2.0, 8.0)}
    
    """
    set1 = set()
    file = open(filename)
    for line in file:
        num = line.split() 
        coordset = float(num[0]), float(num[1])
        set1.add(coordset)
    file.close()
    return set1

m ,b = fit_line_to_points(read_points(input("Please enter the file you would like to read from: ")))
print('The line of best fit is y = '+ str(m) +'x + '+ str(b) +'')
