def bank_statement(list1: list) -> list:
    """
    The function takes a list of floating point numbers, which
    will always have atleast one number. Positive numbers represent
    deposits into a bank account and negative numbers represent withdrawals 
    from the account. The function returns a new list of three numbers: the 
    first will be the sume of the deposits, the second (negative number) will 
    be the sume of the withdrawals, and the third will be the current account
    balance. These numbers will all be rounded to two digits of precision after
    the decimal point.
    
    >>>bank_statement(list1 = [500.99, 600.55, -80.34, -720, 1000])
    [2101.54, -800.34, 1301.2]
    >>>bank_statement(list1 = [600.34, -55.74, -22.54, 65.33])
    [665.67, -78.28, 587.39]
    
    """
    deposits = 0
    withdrawals = 0
    balance = 0 
    if len(list1) >= 1:
        for i in range(len(list1)):
            if list1[i] >= 0:
                deposits = deposits + list1[i] 
            elif list1[i] < 0:
                withdrawals = withdrawals + list1[i]
        balance = deposits + withdrawals
        return [round(deposits, 2), round(withdrawals, 2), round(balance, 2)] 
    else: 
        print("Insufficient Funds")