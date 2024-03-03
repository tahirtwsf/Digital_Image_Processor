def count_evens(list1: list) -> list:
    """
    The function takes a list of integers, which may be empty. 
    The function returns the number of even integers in the list.
    
    >>>count_evens(list1=[1,2,44,6,75,82])
    4
    >>>count_evens(list1=[1,3,5,77,85,2])
    1
    """
    counter = 0
    for i in list1:
        if i % 2 == 0:
            counter += 1
    print (counter)
    
            
        
            
        