def great_42(a:int,b:int) -> bool:
    """
    This function takes two integer values, a and b. 
    It returns True if either value is 42, or if their sum or difference is 42.     
    
    >>>great_42(30,12)
    True
    >>>great_42(52,10)
    True
    >>>great_42(19,42)
    True
    >>>great_42(12.3)
    False
    
    """
    return (42 == a or 42 == b or 42 == (a + b) or 42 == (a - b))
