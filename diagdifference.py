import random

#n = int(input())
arr = []
#for _ in range(n):
#    arr.append(list(map(int,input().split())))

N = 10000
for x in range(N):
    list = []
    for y in range(N):
        if y+1 == N:
            list.append(random.randint(0,9))
            arr.append(list)
        else:
            list.append(random.randint(0,9))
#print (arr)

diag1_sum,diag2_sum = 0,0

for x in range(len(arr)):
    diag1_sum += arr[x][x]
    index = len(arr[x])-x -1
    diag2_sum += arr[x][index]

print (abs(diag1_sum-diag2_sum))

