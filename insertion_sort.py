n = int(input())
arr = list(map(int,input().strip().split(' ')))
insertion_element = arr[-1]
index = len(arr)
inserted = False
index -= 2
while inserted is False and index >= 0:
    if arr[index] > insertion_element:
        arr[index+1] = arr[index]
        index -= 1
    else:
        arr[index+1] = insertion_element
        inserted = True
    print (" ".join(map(str,arr)))

if inserted is False:
    arr[0]=insertion_element
    print (" ".join(map(str,arr)))


