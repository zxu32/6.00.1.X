def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list
        of which item(s) are in each bag.
    """

    # enumerate the 3**N possible combinations
    for i in range(3**len(items)):
        bag1 = []
        bag2 = []
        leftover = items[:]
        for j in range(len(items)):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                bag1.append(items[j])
                leftover.remove(items[j])
        print(leftover)
        for k in range(len(items)):
            print(i >> k)
            if (i >> k) % 2 == 1:
                bag2.append(leftover[k])
        yield (bag1, bag2)

items = ['cat']

test = yieldAllCombos(items)
