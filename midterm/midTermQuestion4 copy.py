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
    increment = 1
    while True:
        # start exponent from 0
        #     if base greater than 1
        #       step exponent up by 1 until base**exponent > num
        #             compare base**exponent - num and base**(exponent -1) - num
        #                 return between exponent and exponent -1 the one with closer approximation to num
        #      if base smaller than 1
        #             step exponent down by 1 until base**exponent > num
        #               compare base**exponent - num and base**(exponent -1) - num
        #                 return between exponent and exponent -1 the one with closer approximation to num
        if num == 1:
            return exponent
        elif num > 1:
            exponent += increment
            if base**exponent - num >= 0:
                if base**exponent - num < num - base**(exponent-1):
                    return exponent
                else:
                    return exponent-1
        else:
            if 1 - num > num:
                return 0
            else:
                return exponent
print(closest_power(20, 210.0))
