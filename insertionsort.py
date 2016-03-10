import random


class InsertionSort(object):
    def __init__(self):
        self.array_to_sort = []
        self.iteration_count=0

    def sort(self,array_to_sort):
        self.array_to_sort = array_to_sort
        for i in range(1,len(self.array_to_sort)):
            self.iteration_count += 1
            curr_value = self.array_to_sort[i]
            j = i
            while j > 0 and self.array_to_sort[j-1] > curr_value:
                self.array_to_sort[j] = self.array_to_sort[j-1]
                j-=1
                self.iteration_count += 1

            self.array_to_sort[j] = curr_value
            print (" ".join(map(str,self.array_to_sort)))

if __name__ == "__main__":
    sorter = InsertionSort()
    array = []
    #for x in range(10):
    #    array.append(random.randint(0,9))
    n = int(input())
    array = list(map(int,input().strip().split(' ')))
    sorter.sort(array)




