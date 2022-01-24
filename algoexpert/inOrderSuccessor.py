# O(n) - time where n is the number of nodes
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    output = []
    findSuccessor_helper(tree, output)
    print(output)
    for idx, val in enumerate(output):
        if val == node.value:
            return BinaryTree(output[idx + 1]) if idx < len(output) - 1 else None
    return None


def findSuccessor_helper(tree, output=[]):
    if tree is None:
        return
    findSuccessor_helper(tree.left, output)
    output.append(tree.value)
    findSuccessor_helper(tree.right, output)
