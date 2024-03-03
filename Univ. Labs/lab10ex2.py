def big_diff(list2: list) -> float:
        """ 
        The function takes a list of integers.
        Assume that the list has at least two 
        integers. The function returns the difference
        between the largest and smallest elements in 
        the list.
        
        >>>big_diff(list2=[10,3,5,6])
        7
        >>>big_diff(list2=[2,5,3,10,15])
        13
        
        """
        big_diff
        maxnum = minnum = list2[0]
        for i in list2:
                if i < minnum:
                        minnum = i
                elif i > maxnum:
                        maxnum = i
        print (maxnum - minnum)
                