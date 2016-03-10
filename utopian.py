n = int(input())
x=1
for _ in range(n):
    N = int(input())
    print(pow(2,(int(N/2) + (N%2))) *x + (pow(2,(int(N/2) + (N%2)))-(N%2+1)))