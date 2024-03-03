def sum3(list5: list) -> float:
    """
    This function takes a list containing three integers.
    The function returns the sum of all the elements.
    
    >>> sum3(list5=[3,5,6])
    14
    >>> sum3(list5=[0,1,1])
    2
    
    """
    if len(list5) == 3:
        return sum(list5)
    else:
        return None
    