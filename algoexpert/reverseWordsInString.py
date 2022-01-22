# O(n) - time
# O(n) - space
def reverseWordsInString(string):
    output = string.split(" ")
    final_output = []
    for idx in range(len(output) - 1, -1, -1):
        final_output.append(output[idx])
    return " ".join(final_output)
