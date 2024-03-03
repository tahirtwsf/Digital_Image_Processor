def make_ends(list12: list) -> list:
    """
    The fucntion takes a list of integers(Assume that the list will not be empty.)
    and returns a new list containing the first and last elements from the original
    list. 
    
    >>>make_ends(list12=[4,5,6,7])
    [4,7]
    >>>make_ends(list12=[0,3,6,0])
    [0,0]
    """
    return [list12[0],list12[-1]]
