# O(n) - time
# O(level) - space
def productSum(array, level=1):
    _sum = 0
    if array:
        for item in array:
            if type(item) == type(list()):
                _sum += productSum(item, level + 1)
            else:
                _sum += item
        return _sum * level
    else:
        return 1
