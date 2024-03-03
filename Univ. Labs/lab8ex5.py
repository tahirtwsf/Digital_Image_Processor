def sum_uniques (a:int, b:int, c:int) ->int:
    """" 
    This function takes three integer values, a, b and c, and returns their sum. 
    However, if one of the values is the same as another of the values, 
    that value is not used when the sum is calculated. if all three values are
    the same, the function returns 0.

    >>>sum_uniques(1,1,2)
    2
    >>>sum_uniques(6,6,6)
    0
    >>>sum_uniques(2,67,545)
    614 
    
    """
    if a==b and a==c and b==c:
        return 0
    elif a==b or a==c or b==c:
        if a==b:
            return c
        elif a==c:
            return b
        elif b==c:
            return a
    else:
        return a+b+c