def divisors(n : int) -> list:
    """
    The function takes a positive integer n and returns a list containing 
    all the positive divisors of n. 
    
    >>>divisors(6)
    [1, 2, 3, 6]
    >>>divisors(9)
    [1, 3, 9]
    
    """
    divisorlist = []
    for i in range(1, n+1):
        if n % i == 0:
            divisorlist += [i]
    return divisorlist
    
        