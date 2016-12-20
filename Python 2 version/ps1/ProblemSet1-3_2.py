#s = ''
s = 'salad hamburger water salad'

def item_order(order):
    currentItem = ''
    itemList = {'salad': 0, 'hamburger': 0, 'water': 0}
    count = 0
    for letter in order:
        count += 1
        currentItem += letter
        if letter == ' ' or count == len(order):
            if letter == ' ':
                currentItem = currentItem[:-1]
            itemList[currentItem] += 1
            currentItem = ''
    print((itemList))
    convert = ' '.join('{}:{}'.format(key, val) for key, val in itemList.items())
    return convert

print(item_order(s))