N = int(input())
arr = map(int, [x for x in input().split()])
positive,negative,zeroes = 0,0,0
for x in arr:
    if x > 0:
        positive += 1
    elif x < 0:
        negative += 1
    else:
        zeroes += 1

print (round(positive/N,6))
print (round(negative/N,6))
print (round(zeroes/N,6))


