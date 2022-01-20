# o(n) - time
# o(1) - space
def kadanesAlgorithm(array):
    max_so_far = array[0]
    max_here = array[0]
    for idx in range(1, len(array)):
        if max_here < 0:
            max_here = 0
        max_here += array[idx]
        max_so_far = max(max_so_far, max_here)
    return (max_so_far)
