# Pythonic way
class MinMaxStack:
    def __init__(self):
        self.stack = []

    def peek(self):
        return self.stack[-1]

    def pop(self):
        return self.stack.pop()

    def push(self, number):
        self.stack.append(number)

    def getMin(self):
        return min(self.stack)

    def getMax(self):
        return max(self.stack)


# Non Pythonic way
class MinMaxStack_2:
    def __init__(self):
        self.stack = []
        self.MinMaxstack = []

    def peek(self):
        # O(1) - time
        # O(1) - space
        return self.stack[-1]

    def pop(self):
        # O(1) - time
        # O(1) - space
        popped_number = self.stack[-1]
        self.stack = self.stack[0:len(self.stack) - 1]
        self.MinMaxstack = self.MinMaxstack[0:len(self.MinMaxstack) - 1]
        return popped_number

    def push(self, number):
        # O(1) - time
        # O(1) - space
        if not self.MinMaxstack:
            self.MinMaxstack.append({
                "min": number,
                "max": number
            })
        else:
            self.MinMaxstack.append(
                {
                    "min": min(self.MinMaxstack[-1]["min"], number),
                    "max": max(self.MinMaxstack[-1]["max"], number),
                }
            )
        self.stack.append(number)

    def getMin(self):
        # O(1) - time
        # O(1) - space
        return self.MinMaxstack[-1]["min"]

    def getMax(self):
        # O(1) - time
        # O(1) - space
        return self.MinMaxstack[-1]["max"]
