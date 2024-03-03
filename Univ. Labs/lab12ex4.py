def sum_x(set1: set) -> float:
    """
    The function takes a set of n points: {(xo, yo,), (x1, y1), ... (xn-1, yn-1)}.
    Each point is represented by a tuple containing two floats. The first and second
    floats are the point's x and y coordinates, respectively. 
    
    >>>sum_x(set1 = {(1,3), (4.5, 6), (1.1, 55)})
    6.6 
    """
    sumx = 0
    for i in set1:
        x, y = i
        sumx += x
    return sumx