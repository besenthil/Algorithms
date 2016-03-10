import random,datetime,heapq
N = int(input())
#array = list(map(int,input().split()))
array = []

print (datetime.datetime.now())
for x in range(1000000):
    heapq.heappush(array, random.randint(1,9))
print (datetime.datetime.now())
print (heapq.heappop(array))
print (heapq.heappop(array))
array = []
print (datetime.datetime.now())
for x in range(1000000):
    array.append(random.randint(1,9))
print (datetime.datetime.now())

'''
print (datetime.datetime.now())
lens = sorted(set(array), reverse = True)
alive = len(array)
while alive != 0:
    print(alive)
    alive -= array.count(lens.pop())
print (datetime.datetime.now())


length = len(array)
print (datetime.datetime.now())
while length >= 1:
    print (length)
    min_element = min(array)
    array = list(filter(lambda x: int(x-min_element) > 0, array ) )
    length = len(array)
print (datetime.datetime.now())
'''


