def genPrimes():
    x = 2
    p = [2]
    while True:
        if all(x%i != 0 for i in p):
            yield p[-1]
            p.append(x)
        x += 1

prime = genPrimes()