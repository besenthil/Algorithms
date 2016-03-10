n = int(input())
for x in range(n):
    on_time = 0
    attendance = []
    students,threshold = list(map(int,input().split()))

    for x in map(int,input().split()):
        if x <= 0:
            on_time += 1

    if on_time < threshold:
        print ("YES")
    else:
        print ("NO")
