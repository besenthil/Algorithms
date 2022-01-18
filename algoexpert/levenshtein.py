# Recursive way
def levenshteinDistance_1(str1, str2):
    print(str1, str2)
    if min(len(str1), len(str2)) == 0:
        return max(len(str1), len(str2))
    elif str1[0] == str2[0]:
        return levenshteinDistance_1(str1[1:], str2[1:])
    else:
        print(str1,str2)
        return 1 + min(levenshteinDistance_1(str1[1:], str2),
                       levenshteinDistance_1(str1[1:], str2[1:]),
                       levenshteinDistance_1(str1, str2[1:])
                       )


# Dynamic Programming way
# O(nm), when n = length of str1 and m = length of str2
def levenshteinDistance_2(str1, str2):
    str1 = str1
    str2 = str2
    dp_array = [[x for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
    for i in range(len(str2) + 1):
        dp_array[i][0] = i
    for i in range(len(str1) + 1):
        dp_array[0][i] = i

    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i - 1] == str1[j - 1]:
                dp_array[i][j] = dp_array[i - 1][j - 1]
            else:
                dp_array[i][j] = 1 + min(dp_array[i][j - 1],
                                         dp_array[i - 1][j],
                                         dp_array[i - 1][j - 1]
                                         )
    return (dp_array[-1][-1])