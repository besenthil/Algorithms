def nodeDepths(root, level=0):
    if root is None:
        return 0
    else:
        return level + nodeDepths(root.right, level + 1) + nodeDepths(root.left, level + 1)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
