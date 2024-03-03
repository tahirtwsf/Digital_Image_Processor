def squirrel_play(temperature: int, summer: bool) -> bool:
    """
    The squirrels in Palo Alto spend most of the day playing. In particular,
    they play if the temperature is between 60 and 90 degrees F (inclusive).
    Unless it is summer, then the upper limit is 100 degrees instead of 90. 
    This function takes two arguments. The first argument is a temperature (an integer). 
    The second argument is a boolean value that specifies the season 
    (True if it's summer, otherwise False). The function returns True if the 
    squirrels are playing, given the temperature and the season.; otherwise it returns False.
    
    >>>squirrel_play(91,True)
    True
    >>>squirrel_play(31, True)
    False
    >>>squirrel_play(110,False)
    False
    
    """
    if 60<=temperature<=90:
        return True 
    elif 90<temperature<=100 and summer==True:
        return True
    else:
        return False
    
    
    
