# O(n) time | O(1) space
def isValidSubsequence(array, sequence):
    sequence_index = array_index = 0
    while sequence_index < len(sequence) and array_index < len(array):
        if sequence[sequence_index] == array[array_index]:
            sequence_index += 1
            array_index += 1
    return sequence_index == len(sequence)

