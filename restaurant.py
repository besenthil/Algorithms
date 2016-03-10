for _ in range(int(input())):
    l,b = list(map(int,input().split()))
    current_number = 1
    largest_number = 1
    for x in range(1,min(l,b)+1):
        max_number = (l*b)/pow(x,2)
        if l%x ==0 and b%x ==0:
            if max_number.is_integer() and x >= current_number:
                current_number = x
                largest_number = max_number
    print (int(largest_number))