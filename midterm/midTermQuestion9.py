
def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    listCopy = []  # the listCopy initiated between different layers of recursion are independent
    for i in aList:
        if isinstance(i, list):  # type(i) == list: also works
            listCopy.extend(flatten(i))  # extend(concatenate as individual elements should be used here instead
            # of append(concatenate as single element)
        else:
            listCopy.append(i)

    return listCopy

print(flatten([[1, [2, 3]], [[4, 5, 6], [7, [8, 9]]], [[3, 2, 1], [2, 1], [1, [0]]]]))
