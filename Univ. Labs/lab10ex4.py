
def centered_average(list3: list) -> float:
    """This function takes a list of integers. 
    Assume that the list has atleast three integers.
    The function returns the centered average of the list. 

    >>> centered_average(list3=[2, 1, 1, 33])
    1.5
    > centered_average(list3=[1, 4, 7, 9, 15, 31])
    8.75
    """
    counter = -1
    average = 0
    for i in list3:
        counter += 1
        average += list3[counter]
        # print(i)
    average -= max(list3)
    average -= min(list3)
    average /= (len(list3) - 2)
    return average


