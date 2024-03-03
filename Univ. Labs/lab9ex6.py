def rotate_left3(list6: list) -> list:
    """
    The function takes a list containing three integers. The function 
    returns a new list containing the same elements, but they are 
    "rotated left". 
    
    >>>rotate_left(list6=[1,2,3])
    [2, 3, 1]
    >>>rotate_left(list6=[2,4,5])
    [4, 5, 2]
    
    """
    
    if len(list6) == 3:
        a = list6[0]
        b = list6[1]
        c = list6[2]
        return [b,c,a]

