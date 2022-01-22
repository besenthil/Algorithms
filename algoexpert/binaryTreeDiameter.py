# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    return diameter(tree)


def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))


def diameter(node):
    if node is None:
        return 0
    return max(height(node.left) +
               height(node.right),
               max(
                   diameter(node.left),
                   diameter(node.right),
               )
               )