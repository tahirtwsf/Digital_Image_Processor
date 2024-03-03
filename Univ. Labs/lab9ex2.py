def same_first_last(list2: list) -> bool:
    """
    The function takes a list of integers. (The list may be empty.) 
    The function returns True if the list is not empty and if the 
    first and last elements are equal. Otherwise, the function returns False.
    
    >>> same_first_last(list2=[2,4,5,5])
    False
    >>> same_first_last(list2=[])
    False
    >>> same_first_last(list2=[2,4,7,5,2])
    True
    """  
    if len(list2) > 0:
        if list2[0]==list2[-1]:
            return True
        else:
            return False
    else:
        return False
    