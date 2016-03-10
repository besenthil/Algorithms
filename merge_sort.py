import random
class MergeSort(object):
    def __init__(self):
        self.counter = 0

    def sort(self,array_to_sort):
        self.counter= self.counter+1
        if len(array_to_sort) <= 1:
            return array_to_sort
        else:
            midpoint= int(len(array_to_sort) / 2)
            left_array = array_to_sort[:midpoint]
            right_array = array_to_sort[midpoint:]

            self.sort(left_array)
            self.sort(right_array)

            i,j,k=0,0,0

            while i < len(left_array) and j < len(right_array):
                if left_array[i] < right_array[j]:
                    array_to_sort[k] = left_array[i]
                    i += 1
                else:
                    array_to_sort[k] = right_array[j]
                    j += 1
                k += 1

            while i < len(left_array):
                array_to_sort[k]=left_array[i]
                i,k=i+1,k+1

            while j < len(right_array):
                array_to_sort[k]=right_array[j]
                j,k=j+1,k+1

            #array_to_sort=left_array+right_array

            return ( array_to_sort)


if __name__ == "__main__":
    array_to_sort = MergeSort()
    array = []
    for x in range(5):
        array.append(random.randint(0,80))
    print(array_to_sort.sort(array),array_to_sort.counter)



