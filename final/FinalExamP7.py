def general_poly(L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    def Sum(base):
        power = len(L) - 1
        result = 0
        for i in L:
            result += i * base**power
            power -= 1
        return result
    return Sum

