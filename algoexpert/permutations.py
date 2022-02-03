# O(n*n!) - time
# O(n*n!) - space
def getPermutations(array):
    if not array:
        return []
    perms = []
    getPermutations_helper(array, [], perms)
    return perms


def getPermutations_helper(array, perm, perms):
    if array is None or array == []:
        perms.append(perm)
    else:
        for index, val in enumerate(array):
            new_array = array[:index] + array[index + 1:]
            new_perm = perm + [array[index]]
            print(index, array, new_perm)
            getPermutations_helper(new_array, new_perm, perms)