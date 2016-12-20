def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing.
    In case of a tie for the longest run, choose the longest run
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run.
    """
    listCopy = L[:]
    monoIncrease = []
    monoDecrease = []
    currentMonoIncrease = [listCopy[0]]
    currentMonoDecrease = [listCopy[0]]
    monoIncreaseEnd = 0
    monoDecreaseEnd = 0

    for i in range(1, len(listCopy)):

        # these codes handles max mono increase
        if listCopy[i] >= listCopy[i-1]:
            currentMonoIncrease.append(listCopy[i])
        if i == len(listCopy)-1:
            if len(monoIncrease) < len(currentMonoIncrease):
                monoIncrease = currentMonoIncrease[:]
                monoIncreaseEnd = i
        if listCopy[i] < listCopy[i-1]:
            if len(monoIncrease) < len(currentMonoIncrease):
                monoIncrease = currentMonoIncrease[:]
                monoIncreaseEnd = i
            currentMonoIncrease = [listCopy[i]]

        # these codes handles mono decrease
        if listCopy[i] <= listCopy[i-1]:
            currentMonoDecrease.append(listCopy[i])
        if i == len(listCopy)-1:
            if len(monoDecrease) < len(currentMonoDecrease):
                monoDecrease = currentMonoDecrease[:]
                monoDecreaseEnd = i
        if listCopy[i] > listCopy[i-1]:
            if len(monoDecrease) < len(currentMonoDecrease):
                monoDecrease = currentMonoDecrease[:]
                monoDecreaseEnd = i
            currentMonoDecrease = [listCopy[i]]

    if len(monoIncrease) > len(monoDecrease):
        return sum(monoIncrease)
    elif len(monoIncrease) < len(monoDecrease):
        return sum(monoDecrease)
    else:
        if monoIncreaseEnd > monoDecreaseEnd:
            return sum(monoDecrease)
        else:
            return sum(monoIncrease)
