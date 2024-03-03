def has23(list13: list) -> bool:
    """
    The function takes a list containing TWO integers and returns True if 
    the list contains a 2 or 3 or both values. Otherwise, the function returns
    False.
    
    >>>has23(list13=[4,5])
    False
    >>>has23(list13=[2,5])
    True
    >>>has23(list13=[4,3])
    True
    >>>has23(list13=[2,3])
    True
    """
    
    if len(list13) == 2:
        if (list13[0] == 2 or list13[1] == 2) or (list13[0] == 3 or list13[1] == 3):
            return True
        else:
            return False
    