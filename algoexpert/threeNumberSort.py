# O(n) - time
def threeNumberSort(array, order):
    counts = [0, 0, 0]
    for number in array:
        counts[order.index(number)] += 1

    idx = 0
    array = []
    while idx < len(order):
        array.append([order[idx]] * counts[idx])
        idx += 1

    return [item for sublist in array for item in sublist]