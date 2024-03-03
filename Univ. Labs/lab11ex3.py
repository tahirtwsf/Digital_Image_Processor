def reverse(list2: list) -> list:
    """
    The function takes a list, which may be empty, and returns
    a new list that contains all the elements of the original list 
    in reverse order.
    
    >>>reverse(list2 = [4, 2, 3, 2] 
    [2, 3, 2, 4] 
    >>>reverse(list2 = [55, 666, 0 ,1])
    [1, 0, 666, 55]
    
    
    
    """
    
    element  =  len(list2)
    reverse_list = [None]*element
    for i in list2:
        element = element - 1
        reverse_list[element] = i
    return reverse_list
    