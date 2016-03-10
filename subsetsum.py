import sys

def subsetsum(array,num):
    if num == 0 or num < 1:
        return None
    elif len(array) == 0:
        return None
    else:
        if array[0] == num:
            return [array[0]]
        else:
            with_v = subsetsum(array[1:],(num - array[0]))
            if with_v:
                return [array[0]] + with_v
            else:
                return subsetsum(array[1:],num)

def recDC(coinValueList,change,knownResults):
   minCoins = change
   if change in coinValueList:
      knownResults[change] = 1
      return 1
   elif knownResults[change] > 0:
      return knownResults[change]
   else:
       for i in [c for c in coinValueList if c <= change]:
         numCoins = 1 + recDC(coinValueList, change-i,
                              knownResults)
         print (numCoins)
         if numCoins < minCoins:
            minCoins = numCoins
            knownResults[change] = minCoins
            #print (knownResults)
   return minCoins


if __name__ == "__main__":
    x = [y for y in range(0,10)]
    coinValueList = [4,5,10,25]
    sys.setrecursionlimit(33000)
    print(recDC(coinValueList,6,[0]*64))
