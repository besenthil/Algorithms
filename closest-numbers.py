N = int(input())
arr = sorted(list(map(int,input().split(' ')))[:N+1])
closest_pairs=[]
min_value = abs(arr[-1]-arr[0])
for x in range(N):
    if x+1 == N:
        pass
    elif (abs(arr[x]-arr[x+1])) < min_value:
        closest_pairs = [x]
        min_value = abs(arr[x]-arr[x+1])
    elif (abs(arr[x]-arr[x+1])) == min_value:
        closest_pairs.append(x)

result = []

for x in closest_pairs:
    result.append(arr[x])
    result.append(arr[x+1])

print (' '.join(map(str,sorted(result))))