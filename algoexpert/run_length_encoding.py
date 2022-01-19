# O(n) - time
# O(1) - space

def runLengthEncoding(string):
    idx = 0
    array = []
    count = 0
    previous_char = string[0]
    if len(string) == 1:
        return "1" + string
    for index, char in enumerate(string[1:]):
        if char == previous_char:
            count += 1
            if count >= 9:
                array.append(str(count) + char)
                count = 0
        else:
            count += 1
            array.append(str(count) + previous_char)
            count = 0
        previous_char = char
        if index == len(string) - 2:
            array.append(str(count + 1) + char)

    return ''.join(array)