LITRES_PER_GALLON = 4.54609
KMS_PER_MILE = 1.60934

def convert_to_litres_per_100_km(mpg):
    return (100 * LITRES_PER_GALLON) / (mpg * KMS_PER_MILE)  
# What value does the function return when the argument is 32? 8.8275512011135
# Is it correct? Yes. 
# What value does the function return when the argument is 0? Returns an error.
# Is it correct? N/A ie. Did not return a value due to error. 
# The function does work for integer arguments (except 0) and real number arguments.
# However, in real life, it does not make sense to use negative numbers for mpg, yet
# the function still returns a value (albeit negative). 