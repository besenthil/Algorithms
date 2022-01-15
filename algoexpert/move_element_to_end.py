# O(n) Time
# O(1) Space
def moveElementToEnd(array, toMove):
    #pythonic way
    current_index = 0
    while current_index < len(array):
        if array[current_index] != toMove:
            array.insert(0, array.pop(current_index))
        current_index += 1
    return array


# O(n) Time
# O(1) Space
def moveElementToEnd_2(array, toMove):
    current_index = 0
    last_index = len(array)-1
    while current_index < last_index:
        if array[last_index] == toMove:
            last_index -= 1
        else:
            if array[current_index] == toMove:
                array[current_index], array[last_index]=array[last_index], array[current_index]
                last_index -= 1
            else:
                current_index += 1
    return array
