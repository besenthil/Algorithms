import datetime
COINS = sorted([4,6,-4,-6,10,2,-2,-10],reverse=True)
change = []

def give_change(COINS,change_due):
    if change_due >= COINS[0]:
        change_due-= COINS[0]
        change.append(COINS[0])
    else:
        COINS = COINS[1:]

    if change_due >= 0:
        give_change(COINS,change_due)
    else:
        return []

    return change

def pickBest(coins,due):
     if due == 0: return []
     for c in coins:
        if c<= due: return [c] + pickBest(coins,due-c)

print(give_change(COINS,41))
#print(pickBest(COINS,200))



