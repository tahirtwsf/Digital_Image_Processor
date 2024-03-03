import math

def factorial( n: int ) -> int:
    """Return n! for positive values of n.
    
    >>> factorial(1)
    1
    >>> factorial(2)
    2
    >>> factorial(3)
    6
    >>> factorial(4)
    24
    """
    fact = 1
    for i in range( 2, n + 1 ):
        fact = fact * n
        
    return fact

def testing( startNum: int, endNum: int ):
    """This function checks whether or not factorial returns the proper factorial"""
    tPass = 0
    tFail = 0
    counter = startNum
    while counter <= endNum:
        expectedres = math.factorial(counter)
        realres = factorial(counter)
        if expectedres == realres:
            tPass += 1
            print('Testing Factorial(', counter, ')', '\n'
                  'Expected result: ', expectedres, ' Actual Result: ', realres, '\n'
                  'Test Passed', sep = '')
            
        else:
            tFail += 1
            print('Testing Factorial(', counter, ')', '\n'
                  'Expected result: ', expectedres, ' Actual Result: ', realres, '\n'
                  'Test Failed', '\n', sep = '')            
        counter += 1
    print( tPass, ' tests passed', '\n',
           tFail, ' tests failed', sep = '')

# runs testing when program is run    
testing( 1, 4 )