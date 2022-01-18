# O(v+e) - time
# O(v) - space
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        to_be_processed_queue = []
        array.append(self.name)
        return self.breadthFirstSearch_helper(array, self.children, to_be_processed_queue)

    def breadthFirstSearch_helper(self, array, children, to_be_processed_queue):
        for child in children:
            to_be_processed_queue.insert(0, child)
        while to_be_processed_queue:
            item = to_be_processed_queue.pop()
            array.append(item.name)
            self.breadthFirstSearch_helper(array, item.children, to_be_processed_queue)
        return array
