def accumulated_amount(principal, rate, n, time):
    return principal * (1 + rate/n)**(n*time)
# What value would you expect the function to return if the principal is $0? 0.0
# Does your function return correct value for this principal? Yes
# What value would you expect the function to return if the interest is 0%? 1500.0
# Does your function return correct value for this interest rate? Yes.
