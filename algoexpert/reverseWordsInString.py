# O(n) - time
# O(n) - space
def reverseWordsInString(string):
    output = string.split(" ")
    final_output = []
    for idx in range(len(output) - 1, -1, -1):
        final_output.append(output[idx])
    return " ".join(final_output)


# O(n) - time
# O(n) - space
def reverseWordsInString(string):
    prev_idx = 0
    output = []
    final_output = []
    for idx, char in enumerate(string):
        if char == " " or idx == len(string) - 1:
            if idx == len(string) - 1:
                idx += 1
            output.append(string[prev_idx:idx])
            prev_idx = idx + 1

    for idx in range(len(output) - 1, -1, -1):
        final_output.append(output[idx])
    return " ".join(final_output)