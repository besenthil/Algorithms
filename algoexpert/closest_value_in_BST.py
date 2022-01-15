# Time complexity
#     Worst case - O(n)
#     Average case - O(logn)

# Space complexity
#     Worst case - O(1)
#     Average case - O(1)

def findClosestValueInBst_1(tree, target):
	current_node = tree
	current_closest_value = float("inf")
	closest_node = None
	while current_node:
		if abs(target - current_node.value) < current_closest_value:
			current_closest_value = abs(target - current_node.value)
			closest_node = current_node
		if target > current_node.value:
			current_node = current_node.right
		elif target < current_node.value:
			current_node = current_node.left
		else:
			return current_node.value
	return closest_node.value


# Time complexity
#     Worst case - O(n)
#     Average case - O(logn)

# Space complexity
#     Worst case - O(n)
#     Average case - O(logn)

def findClosestValueInBst_2(tree, target):
	closest = float("inf")
	return findClosestValueInBstHelper(tree, target, closest)


def findClosestValueInBstHelper(tree, target, closest):
	if tree is None:
		return closest
	else:
		if abs(target - closest) > abs(target - tree.value):
			closest = tree.value
		if target < tree.value:
			return findClosestValueInBstHelper(tree.left, target, closest)
		elif target > tree.value:
			return findClosestValueInBstHelper(tree.right, target, closest)
		else:
			return tree.value


# This is the class of the input tree. Do not edit.
class BST:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None