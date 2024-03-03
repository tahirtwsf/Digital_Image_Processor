from typing import List
def average(list1: List[tuple]) -> List[tuple]:
    """
    The function takes a list of tuples, and each tuple contains three 
    non-negative integers. The function returns a new list of tuples. The 
    three numbers in each tuple are the integer average values of the numbers
    in the tuple at the same position in the original list.
    
    >>>average(list1 = [(27,219,134), (2,3,5), (3,55,67)]
    [(126, 126, 126), (3, 3, 3), (41, 41, 41)]
    """
    list2 = []
    for i in range(len(list1)):
        mean = (list1[i][0] + list1[i][1] + list1[i][2]) // 3
        list2.append((mean, mean, mean))
    return list2
    