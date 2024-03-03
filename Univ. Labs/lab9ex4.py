def common_end(list3: int, list4: int) -> bool:
    """
    The function takes two lists of integers that are not empty, but which may have different lengths.
    The function returns True if they have the same first element or the same last element 
    or if the first and last elements of both lists are the same. Otherwise, the function returns False.
    
    >>>common_end(list3=[1,3,2,3],list4=[2,4,6,3,1])
    False
    >>>common_end(list3=[1,3,2,1],list4=[2,4,6,3,1])
    True
    >>>common_end(list3=[1,3,2,2],list4=[1,4,6,3,2])
    True
    
    """
    if len(list3) and len(list4) > 0:
        if list3[0] == list4[0] or list3[-1] == list4[-1]:
            return True
        else:
            return False
    