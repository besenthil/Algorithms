N,T=(map(int,input().split()))
width=list(map(int,input().split()))
for _ in range(T):
    start,end = tuple(map(int,input().split()))
    print(min(width[start:end+1]))

