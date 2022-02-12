class ContinuousMedianHandler:
    def __init__(self):
        # Write your code here.
        self.median = None
        self.num_arr = []
        self.low_index = 0

    # O(nlogn) - time
    # O(n) - space
    def insert(self, number):
        self.num_arr.append(number)
        self.num_arr.sort()
        if len(self.num_arr) > 2 and len(self.num_arr) % 2 == 1:
            self.low_index += 1
        if len(self.num_arr) % 2 == 0:
            self.median = (self.num_arr[self.low_index] + self.num_arr[self.low_index + 1]) / 2
        else:
            self.median = self.num_arr[self.low_index]

    def getMedian(self):
        return self.median
