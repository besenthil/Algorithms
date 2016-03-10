import random,datetime

def partition(arr,low,high):
    pivot = arr[low]
    i = low
    j = high

    while i < j:
        while ((i <= high) and (arr[i] <= pivot)):
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i],arr[j] = arr[j],arr[i]
        else:
            break

    arr[low]=arr[j]
    arr[j] = pivot
    print (arr[low:pivot])

    return j

def quick_sort_recursive(arr,low,high):
    if high > low:
        #print(arr)
        pivot = partition(arr,low,high)
        quick_sort_recursive(arr,low,pivot-1)
        quick_sort_recursive(arr,pivot+1,high)


def quick_sort(arr):
    quick_sort_recursive(arr,0,len(arr)-1)
    #print (arr)

if __name__ == '__main__':
    N = int(input())
    arr = list(map(int,input().split(' ')))[:N+1]
    quick_sort(arr)
    print (arr)