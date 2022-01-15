# O(n) time | O(1) space
def isPalindrome_1(string):
	left = 0
	right = len(string) - 1
	while left < right :
		if string[left] == string[right]:
			left += 1
			right -= 1
		else:
			return False
	return True


# O(n) time | O(n) space
def isPalindrome_2(string):
	if string == '':
		return True
	else:
		return string and string[0] == string[-1] and isPalindrome_2(string[1:-1])