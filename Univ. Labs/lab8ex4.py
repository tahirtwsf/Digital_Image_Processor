def blackjack(a:int, b:int) -> int:
    """ 
    This function takes two positive integer values, a and b. 
    The function returns whichever value is closest to 21 
    without being over 21. It returns 0 if both values are over 21. 
    
    >>>blackjack(3,25)
    3
    >>>blackjack(18,21)
    21
    >>>blackjack(25,30)
    0 
    
    """
    if a<=21 and b<=21:
        if b>a:
            return b
        elif a>b:
            return a
    elif a<=21 or b<=21:
        if a<21 and b>21:
            return a
        elif a>21 and b<21:
            return b
    elif a>21 or b>21:
        if a>21 and b>21:
            return 0
        elif a>21 or b<21:
            return b
        elif a<21 or b>21:
            return a 

    
        
    
