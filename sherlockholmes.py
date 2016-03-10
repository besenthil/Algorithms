from collections import Counter

n = int(input())
decent_numbers = []

for x in range(n):
    digits = int(input().strip())
    decent = '5'*digits
    condition = False
    digits_3 = 0
    start_len = len(decent_numbers)
    while condition is False:

        decent = [x for x in decent]
        count = dict(Counter(decent))
        if count.get('3') is None:
            count['3'] = 0
        if count.get('5') is None:
            count['5'] = 0

        if (count['3'] % 5 == 0 ) and (count['5'] % 3 == 0):
            decent_numbers.append(count)
            condition=True

        digits -= 1
        digits_3 += 1
        decent =  '5'*digits + '3'*digits_3

        if digits < 0:
            condition = True
            if start_len == len(decent_numbers):
                decent_numbers.append('-1')


for x in decent_numbers:
    if x == '-1':
        print (x)
    else:
        print ('5'*x['5'] + '3'*x['3'])

