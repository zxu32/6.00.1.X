s1 = 'water salad hamburger salad'


def item_order(order):

    currentItem = ''
    saladCount = 0
    hamburgerCount = 0
    waterCount = 0

    for letter in order:
        currentItem += letter
        currentItem = currentItem.replace(' ', '')
        if currentItem == 'salad':
            saladCount += 1
            currentItem = ''
        if currentItem == 'hamburger':
            hamburgerCount += 1
            currentItem = ''
        if currentItem == 'water':
            waterCount += 1
            currentItem = ''

    return 'salad:{} hamburger:{} water:{}'.format(saladCount, hamburgerCount, waterCount)


print(item_order(s1))