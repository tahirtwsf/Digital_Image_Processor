def has22(list3: list) -> bool:
    """
    The function takes a list of integers, which
    may be empty. The function returns True
    if the list contains a 2 next to 2. Other-
    wise, the function returns False.
    
    >>>has22(list3=[1,2,2,3])
    True
    >>>has22(list3=[4,2,3,2])
    False
    """
    if len(list3) == 1:
        return False    
    elif len(list3) >= 1:   
        for i in list3:
            if ', 2, 2' in str(list3):
                return True
            elif list3[0] == 2 and list3[1] == 2:
                return True
            else:
                return False
    else: 
        return False
        
      