for _ in range(int(input())):
    N = int(input())
    print (len([digit for digit in map(int,[x for x in str(N)]) if digit != 0 and N%digit == 0]))




