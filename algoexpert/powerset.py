# O(n*2^n) - time
# O(n) - space

def powerset(array):
    subsets = [[]]
    powerset_helper(array, subsets)
    return subsets


def powerset_helper(array, subsets):
    for i in range(len(array)):
        if array[:i] not in subsets:
            subsets.append(array[:i])
            powerset_helper(array[:i], subsets)
        if array[i:] not in subsets:
            subsets.append(array[i:])
            powerset_helper(array[i:], subsets)
    print(subsets)

    for i in range(len(array)):
        if array[:i] + array[i + 1:] not in subsets:
            subsets.append(array[:i] + array[i + 1:])
            powerset_helper(array[:i] + array[i + 1:], subsets)
