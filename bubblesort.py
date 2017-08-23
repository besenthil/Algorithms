import random


class BubbleSort(object):
    def __init__(self):
        self.array_to_sort = []
        self.iteration_count=0

    def sort(self,array_to_sort):
        self.array_to_sort = array_to_sort
        for repetitions in range(0,len(self.array_to_sort)):
            low = 0
            high = 1
            while high <= len(self.array_to_sort)-1:
                if self.array_to_sort[low] > self.array_to_sort[high]:
                    self.array_to_sort[low],self.array_to_sort[high]=self.array_to_sort[high],self.array_to_sort[low]
                high = high + 1
                low = low + 1

                print (self.array_to_sort)



if __name__ == "__main__":
    sorter = BubbleSort()
    array = []
    #for x in range(10):
    #    array.append(random.randint(0,9))
    n = int(input())
    array = list(map(int,input().strip().split(' ')))
    sorter.sort(array)
