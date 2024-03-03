def first_last6(list1: list) -> bool:
    """
    This function takes a list of integers
    (assume that the list will not be empty).
    The function returns True if a 6 is the 
    first element or the last element or if
    both the first and last element are 6. 
    Otherwise, the function returns False.
    
    >>> first_last6(list1 = [6,1,4,2,4,7,88,5,3,6])
    True
    >>> first_last6(list1 = [6,1,4,2,4,7,88,5,3,7])
    True
    >>> first_last6(list1 = [5,1,6,2,9,3,8,5,4,10])
    False
    """
    if list1[0]==6 or list1[-1]==6:
        return True
    else:
        return False
    
