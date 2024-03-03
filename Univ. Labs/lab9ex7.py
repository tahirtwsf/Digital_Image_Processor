def reverse3(list7:list) -> list:
    """
    The function takes a list containing three integers.
    The function returns a new list containing the same 
    elements in reverse order.
    
    >>>reverse3(list7=[1,2,3])
    [3, 2, 1]
    
    """
    if len(list7) == 3:
        a = list7[0]
        b = list7[1]
        c = list7[2]
        return [c,b,a]
    