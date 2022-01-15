# O(nlogn) Time
# O(n) Space
def sortedSquaredArray(array):
    return sorted(x ** 2 for x in array)