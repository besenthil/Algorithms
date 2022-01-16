# O(n) - time
# O(n) - space

def isMonotonic(array):
    idx = 0
    trend = []
    while idx < len(array) - 1:
        if array[idx] > array[idx + 1]:
            trend.append(1)
        elif array[idx] < array[idx + 1]:
            trend.append(0)
        elif array[idx] == array[idx + 1] and idx == 0:
            trend.append(-1)
        else:
            trend.append(trend[idx - 1])
        idx += 1
    idx = 0
    while idx < len(trend) - 1:
        if trend[idx] != trend[idx + 1] and (trend[idx] != -1 and trend[idx + 1] != -1):
            return False
        idx += 1
    return True
