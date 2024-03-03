def coupon(amount_spent: float) -> float:
    """
    Return a coupon value based on the amount spent and coupon percentages
    >>> coupon(210)
    25.2
    >>> coupon(130)
    13.0
    >>> coupon(15)
    1.2
    """
    if amount_spent < 10:
        couponValue = amount_spent * 0

    elif amount_spent < 60:
        couponValue = amount_spent * 0.08

    elif amount_spent <= 150:
        couponValue = amount_spent * 0.1

    elif amount_spent <= 210:
        couponValue = amount_spent * 0.12

    elif amount_spent > 210:
        couponValue = amount_spent * 0.14

    return couponValue