# O(logn) - time
# O(logn) - space

def binarySearch(array, target):
    return binarySearch_helper(array, target, 0, len(array) - 1)


def binarySearch_helper(array, target, start, end):
    if start > end:
        return -1
    mid = int((start + end) / 2)
    if target == array[mid]:
        return mid
    elif target < array[mid]:
        return binarySearch_helper(array, target, start, mid - 1)
    else:
        return binarySearch_helper(array, target, mid + 1, end)