# O(n^2) - time
# O(1) - space
def selectionSort(array):
    idx = 0
    while idx < len(array) - 1:
        running_min_idx = idx
        inner_idx = idx + 1
        while inner_idx < len(array):
            if array[running_min_idx] > array[inner_idx]:
                running_min_idx = inner_idx
            inner_idx += 1
        array[idx], array[running_min_idx] = array[running_min_idx], array[idx]
        idx += 1
    return array
