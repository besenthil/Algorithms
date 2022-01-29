# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    left_index = linkedList
    while left_index:
        right_index = left_index.next
        while right_index and left_index.value == right_index.value:
            right_index = right_index.next
        left_index.next = right_index
        left_index = right_index
    return linkedList
