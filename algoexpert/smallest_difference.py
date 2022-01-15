# O(n^2) time | O(1) space
def smallestDifference(arrayOne, arrayTwo):
    least_difference = None
    least_diff_set = []
    for i in arrayOne:
        for j in arrayTwo:
            abs_difference = getAbsoluteDifference(i, j)
            if least_difference is None:
                least_difference = abs_difference
            else:
                if abs_difference < least_difference:
                    least_difference = abs_difference
                    least_diff_set = [i, j]
    return least_diff_set


def getAbsoluteDifference(num1, num2):
    return max(num1, num2) - min(num1, num2)


# O(nlogn) + (mlogm) + o(n) time | o(n) space
def smallestDifference(arrayOne, arrayTwo):
    def get_right_position_index():
        return [sorted_array[ptr] if bitmap[ptr] == 1 else sorted_array[ptr + 1],
                sorted_array[ptr] if bitmap[ptr] == 0 else sorted_array[ptr + 1]]

    sorted_array = sorted(arrayOne + arrayTwo)
    bitmap = []
    ptr = 0
    least_diff = float("inf")
    output = []
    for idx, val in enumerate(sorted_array):
        if val in arrayOne:
            bitmap.append(1)
            arrayOne.remove(val)
        else:
            bitmap.append(0)
    while ptr < len(sorted_array) - 1:
        if bitmap[ptr] != bitmap[ptr + 1]:
            difference = sorted_array[ptr + 1] - sorted_array[ptr]
            if difference <= least_diff:
                least_diff = difference
                output = get_right_position_index()
        ptr = ptr + 1
    return output
