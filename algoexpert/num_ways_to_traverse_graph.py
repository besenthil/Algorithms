# O(2^(n+m) - time
# O(n+m) - space
def numberOfWaysToTraverseGraph(width, height):
	if width > 1 and height >1:
		return numberOfWaysToTraverseGraph(width-1, height) + numberOfWaysToTraverseGraph(width, height-1)
	else:
		return 1