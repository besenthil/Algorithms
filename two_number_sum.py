# O(n^2) time | O(1) space
def twoNumberSum_1(array, targetSum):
	for i in array:
		for j in array:
			if i == j:
				break
			if i + j == targetSum:
				return [i, j]
	return []

# O(n) time | O(1) space
def twoNumberSum_2(array, targetSum):
	for number in array:
		result = targetSum - number
		if (result) in array and result != number:
			return [number,array[array.index(targetSum - number)]]
	return []


# O(nlogn) time | O(1) space
def twoNumberSum_3(array, targetSum):
	array.sort()
	left = 0
	right = len(array) - 1
	while (left < right):
		_sum = array[left] + array[right]
		if _sum == targetSum:
			return [array[left],array[right]]
		elif _sum < targetSum:
			left = left + 1
		elif _sum > targetSum:
			right = right - 1
	return []


