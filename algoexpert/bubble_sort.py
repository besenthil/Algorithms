# Average O(n^2) - time | O(n) - space
def bubbleSort(array):
    last_sorted_index = len(array) - 1
    is_sorted = True
    while last_sorted_index >= 0 and is_sorted:
        index = 0
        is_sorted = False
        while index < last_sorted_index:
            if array[index] > array[index + 1]:
                array[index], array[index + 1] = array[index + 1], array[index]
                is_sorted = True
            index += 1
        last_sorted_index -= 1
    return array
