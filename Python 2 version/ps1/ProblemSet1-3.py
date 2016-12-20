#s = ''
s = 'apple banana apple banana peach'


def item_order(order):
    currentItem = ''
    itemList = {}
    count = 0
    for letter in order:
        count += 1
        currentItem += letter
        if letter == ' ' or count == len(order):
            if letter == ' ':
                currentItem = currentItem[:-1]
            if currentItem not in itemList:
                itemList[currentItem] = 1
                currentItem = ''
            else:
                itemList[currentItem] += 1
                currentItem = ''
    return itemList
    #for i, j in itemList.items():
     #   return(i, ':', j)
    #return output

item_order(s)