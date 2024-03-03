def sum2(list9: list) -> int:
    """
    The function takes a list of integers and
    returns the sum of the first two list elements.
    It should return 0 if the list is empty, or the 
    element if the list has one element.
    
    >>>sum2(list9=[1,4,5,6,7])
    5
    >>>sum2(list9=[3])
    3
    >>>sum2(list9=[])
    0
    
    
    """
    if len(list9) > 1:
        return list9[0] + list9[1]
    elif len(list9) == 1:
        return list9[0]
    else:   
        return 0