# O(n^3) time | O(n) space
def threeNumberSum_1(array, targetSum):
	triplets = []
	for a in array:
		for b in array:
			for c in array:
				if a == b or b == c or a == c:
					pass
				elif a + b + c == targetSum:
					if sorted([a,b,c]) in triplets:
						pass
					else:
						triplets.append(sorted([a,b,c]))
	return sorted(triplets)


# O(n^2) time | O(n) space
def threeNumberSum_2(array, targetSum):
	triplets = []
	for a in array:
		for b in array:
			if a != b:
				result = targetSum - (a+b)
				if (result in array) and sorted([a,b,result]) not in triplets and result not in [a,b]:
					triplets.append(sorted([a,b,result]))
	return sorted(triplets)


# O(n^2) time | O(n) space
def threeNumberSum_3(array, targetSum):
	array.sort()
	match_sum_found = []
	for a in range(len(array)):
		left = a + 1
		right = len(array) - 1
		while left < right :
			_sum = array[left] + array[right] + array[a]
			if _sum == targetSum:
				match_sum_found.append([array[a], array[left], array[right]])
				left = left + 1
				right = right - 1
			elif _sum < targetSum:
				left = left + 1
			elif _sum > targetSum:
				right = right - 1

	return match_sum_found


array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0
assert (threeNumberSum_1(array,targetSum)) == [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
assert (threeNumberSum_2(array,targetSum)) == [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
assert (threeNumberSum_3(array,targetSum)) == [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
