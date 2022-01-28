# O(n) - time
# O(n) - space

def maxSubsetSumNoAdjacent(array):
    if not array:
        return 0
    if len(array) == 1:
        return array[0]
    max_sub_sum_array = [array[0], max(array[0], array[1])]
    for ind in range(2, len(array)):
        max_sub_sum_array.append(max(array[ind] + max_sub_sum_array[ind - 2],
                                     max_sub_sum_array[ind - 1]
                                     ))
    return max_sub_sum_array[-1]
