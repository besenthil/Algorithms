# o(n*d) - time
# o(n) - space
def numberOfWaysToMakeChange(n, denoms):
    possibilities = [0] * (n + 1)
    possibilities[0] = 1
    for denom in denoms:
        for index, value in enumerate(possibilities):
            if index > 0 and index >= denom:
                possibilities[index] += possibilities[index - denom]
    return possibilities[-1]
