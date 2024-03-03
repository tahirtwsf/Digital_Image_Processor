def middle_way(list10: list, list11: list) -> list:
    """
    The function takes two lists that each contain three integers.
    The function returns a new list containing their middle elements. 
    
    >>>middle_way(list10=[3,4,6],list11=[6,5,4])
    [4, 5]
    >>>middle_way(list10=[3,0,6],list11=[6,0,4])
    [0, 0]
    """
    if len(list10) == 3 == len(list11):
        return [list10[1],list11[1]]
    