# O(n) time| O(n) space
# Using a dictionary
def firstDuplicateValue_1(array):
    hash_set = dict()
    for i in array:
        if hash_set.get(i, None) is not None:
            return i
        else:
            hash_set[i] = 0
    return -1


# O(n) time| O(1) space
# Mutating the list
def firstDuplicateValue_2(array):
    for value in array:
        absvalue = abs(value)
        print(absvalue)
        if array[absvalue - 1] < 0:
            return absvalue
        array[absvalue - 1] *= -1
    return -1
