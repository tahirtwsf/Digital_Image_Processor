
def bakers_party(number_of_pastries:int, isweekend:bool)-> bool: 
    """
    When bakers get together for a party, they like to eat pastries. 
    A bakers' party is successful when the number of pastries is between 40 and 60, inclusive. 
    Unless it is the weekend, in which case there is no upper bound on the number of pastries. 
    This function takes two arguments.The first argument is the number of pastries (an integer). 
    The second argument is True if it's the weekend, False if the day is a weekday. 
    The function returns True if a party with the given arguments is successful, 
    otherwise it will return False.
    
    >>>bakers_party(45,False)
    True
    >>>bakers_party(95,False)
    False
    >>>bakers_party(61,True)
    True
    
    """
    if 40 <= number_of_pastries <=60:
        return True
    elif number_of_pastries > 60 and isweekend==True:
        return True
    else:
        return False
        
    


