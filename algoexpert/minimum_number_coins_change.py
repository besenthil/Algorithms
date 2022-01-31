# O(nd) - time
# O(n) - space
def minNumberOfCoinsForChange(n, denoms):
    num_coins = [float("inf") for amt in range(n + 1)]
    num_coins[0] = 0
    for denom in denoms:
        for num_coin in range(len(num_coins)):
            if denom <= num_coin:
                num_coins[num_coin] = min(num_coins[num_coin],
                                          num_coins[num_coin - denom] + 1)
    return num_coins[n] if num_coins[n] != float("inf") else -1
