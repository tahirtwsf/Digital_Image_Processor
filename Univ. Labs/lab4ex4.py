import math 
def area_of_cone(height, radius):
    return (math.pi*radius)*math.sqrt(radius**2 + height**2)
# First Test: 
# Radius: 5
# Height: 10
# Calculatd Area: 175.62
# Program Calculated Area: 175.62036827601816
# Second Test: 
# Radius: 10
# Height: 15
# Calculated Area: 566.36
# Program Calulated Area: 566.3586699569488 
# For both of my test cases, the actual result of the lateral surface area was 
# the same as the expected result.