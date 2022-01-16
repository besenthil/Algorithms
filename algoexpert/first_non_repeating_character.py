# O(n^2) - time
# O(1) - space
def firstNonRepeatingCharacter_1(string):
    for x_idx, x_val in enumerate(string):
        found_repeats = False
        for y_idx, y_val in enumerate(string):
            if x_idx != y_idx and x_val == y_val:
                found_repeats = True
        if not found_repeats:
            return x_idx
    return -1


# O(n) - time
# O(n) - space

def firstNonRepeatingCharacter_2(string):
    hashset = dict()
    for a in string:
        hashset[a] = hashset.setdefault(a, 0) + 1
    for item, count in (hashset.items()):
        print(item, count)
        if count == 1:
            return string.index(item)
    return -1
