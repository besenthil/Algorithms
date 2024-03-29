# O(n) - time
# O(n) - space

def invertBinaryTree(tree):
    if tree is None:
        return
    tree.left, tree.right = invertBinaryTree(tree.right), invertBinaryTree(tree.left)
    return tree


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
