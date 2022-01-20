# O(n) - time
# O(n) - space

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    array = []
    branchSums_helper(root, array, 0)
    return array


def branchSums_helper(root, array=[], _sum=0):
    if root is None:
        return

    _sum += root.value
    if root.left is None and root.right is None:
        array.append(_sum)
        return
    branchSums_helper(root.left, array, _sum)
    branchSums_helper(root.right, array, _sum)
