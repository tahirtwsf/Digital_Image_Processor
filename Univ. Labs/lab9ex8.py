def max_end3(list8: list) -> list:
    """
    The function takes a list containing three integers
    and determines which element is larger: the first
    or the last element. It returns a new list which all
    the elements are initialized to that value.
    
    >>> max_end3(list8=[1,4,6])
    [6, 6, 6]
    >>> max_end3(list8=[3,4,1])
    [3, 3, 3]
    """
    if len(list8) == 3:
        if list8[0] > list8[-1]:
            return [list8[0],list8[0], list8[0]]
        elif list8[0] < list8[-1]:
            return [list8[-1],list8[-1], list8[-1]]

        