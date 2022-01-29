# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    return validateBst_helper(tree, float("-inf"), float("inf"))


def validateBst_helper(tree, min_value, max_value):
    if tree is None:
        return True
    if tree.value < min_value or tree.value >= max_value:
        return False
    return validateBst_helper(tree.left, min_value, tree.value) and validateBst_helper(tree.right, tree.value,
                                                                                       max_value)