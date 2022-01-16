# O(n^2) time | O(n) space
def insertionSort_1(array):
    current_idx = 1
    while current_idx < len(array):
        while current_idx > 0 and array[current_idx - 1] > array[current_idx]:
            swap_item = array.pop(current_idx)
            array.insert(current_idx - 1, swap_item)
            current_idx -= 1
        current_idx += 1
    return array


# O(n^2) time | O(n) space
def insertionSort_2(array):
    current_idx = 1
    while current_idx < len(array):
        swap_idx = current_idx
        while swap_idx > 0 and array[swap_idx - 1] > array[swap_idx]:
            array[swap_idx], array[swap_idx - 1] = array[swap_idx - 1], array[swap_idx]
            swap_idx -= 1
        current_idx += 1
    return array
