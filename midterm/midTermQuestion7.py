def f(int1, int2):
    return int1 > int2

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    inersect = {}
    diff = {}
    for i in d1:
        if i in d1.keys() & d2.keys():
            inersect[i] = f(d1[i], d2[i])
        else:
            diff[i] = d1[i]
    for j in d2:
        if j not in d1.keys() & d2.keys():
            diff[j] = d2[j]
    return inersect, diff

d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}

print(dict_interdiff(d1, d2))
