# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# o(n) - time
def reconstructBst(preOrderTraversalValues):
    head = BST(preOrderTraversalValues[0])
    idx = 1
    while idx < len(preOrderTraversalValues):
        traverse_bst(head, preOrderTraversalValues[idx])
        idx += 1
    return head


def traverse_bst(tree, val):
    if tree is None:
        return
    else:
        if val < tree.value and tree.left is None:
            tree.left = BST(val)
        elif val < tree.value and tree.left is not None:
            traverse_bst(tree.left, val)
        elif val >= tree.value and tree.right is None:
            tree.right = BST(val)
        elif val >= tree.value and tree.right is not None:
            traverse_bst(tree.right, val)
