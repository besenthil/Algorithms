# O(n) - time, n = nodes
# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    sorted_array = []
    findKthLargestValueInBst_helper(tree, sorted_array)
    return sorted_array[-k]


def findKthLargestValueInBst_helper(tree, sorted_array):
    if tree is None:
        return
    findKthLargestValueInBst_helper(tree.left, sorted_array)
    sorted_array.append(tree.value)
    findKthLargestValueInBst_helper(tree.right, sorted_array)
