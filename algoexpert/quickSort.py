# O(nlogn) - time
# O(nlogn) - time
def quickSort(array):
    quickSortHelper(array, 0, len(array) - 1)
    return array


def quickSortHelper(array, start_index, end_index):
    if start_index >= end_index:
        return
    left_index = start_index + 1
    right_index = end_index
    pivot_index = start_index
    while right_index >= left_index:
        if array[pivot_index] < array[left_index] and array[pivot_index] > array[right_index]:
            swap(left_index, right_index, array)
        if array[left_index] <= array[pivot_index]:
            left_index += 1
        if array[right_index] >= array[pivot_index]:
            right_index -= 1
    swap(pivot_index, right_index, array)
    quickSortHelper(array, right_index + 1, end_index)
    quickSortHelper(array, start_index, right_index - 1)


def swap(left_index, right_index, array):
    array[left_index], array[right_index] = array[right_index], array[left_index]