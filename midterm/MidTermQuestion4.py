def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    exponent = 0
    increment = 0.0001
    while True:
        if num == 1:
            return exponent
        elif num < 1:
            exponent -= increment
            if num - base**exponent >= 0:
                return round(exponent, 0)
        else:
            exponent += increment
            if num - base**exponent <= 0:
                print(exponent, base**exponent)
                return round(exponent, 0)

print(closest_power(4, 160))
