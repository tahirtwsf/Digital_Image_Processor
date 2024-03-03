 
def tip(meal_Cost: float, satisfaction: int) -> float:
    """
    Return a tip amount based on diner' satisfaction based
    on predefined tip percentages
    >>> tip(20, 1)
    4.0
    >>> tip(60, 2)
    9.0
    """
    if satisfaction == 1:
        return meal_Cost * 0.2

    elif satisfaction == 2:
        return meal_Cost * 0.15

    elif satisfaction == 3:
        return meal_Cost * 0.05        

    else:
        return  print("Please use a valid satisfaction rating (1,2,3)")