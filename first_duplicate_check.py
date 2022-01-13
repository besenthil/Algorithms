# O(n) time| O(n) space
# Using a dictionary
def firstDuplicateValue(array):
    hash_set = dict()
    for i in array:
        if hash_set.get(i, None) is not None:
            return i
        else:
            hash_set[i] = 0
    return -1
