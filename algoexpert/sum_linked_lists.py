# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    ll_one = []
    ll_two = []
    while (linkedListOne is not None):
        ll_one.append(linkedListOne.value)
        linkedListOne = linkedListOne.next
    ll_one.reverse()
    ll_one_number = int(''.join([str(int) for int in ll_one]))
    while (linkedListTwo is not None):
        ll_two.append(linkedListTwo.value)
        linkedListTwo = linkedListTwo.next
    ll_two.reverse()
    ll_two_number = int(''.join([str(int) for int in ll_two]))
    out = list(map(int, str(ll_one_number + ll_two_number)))
    out.reverse()
    head = LinkedList(out[0])
    pointer = head
    index = 0
    while index < len(out) - 1:
        index += 1
        pointer.next = LinkedList(out[index])
        pointer = pointer.next
    return head
