# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) - time
def removeKthNodeFromEnd(head, k):
    node_position_to_remove = get_length_of_linked_list(head) - k + 1
    start = 0
    node = head
    if node_position_to_remove == 1:
        while node.next:
            node.value = node.next.value
            previous_node = node
            node = node.next
        previous_node.next = None
        node = None
    else:
        while start < node_position_to_remove - 2:
            node = node.next
            start += 1
        node.next = node.next.next
    return head


def get_length_of_linked_list(head):
    node = head
    length = 1
    while node.next:
        node = node.next
    length += 1
    return length