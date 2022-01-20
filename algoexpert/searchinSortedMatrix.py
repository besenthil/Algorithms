# O(mn) - time, m = rows, n = cols
# O(1) - space
def searchInSortedMatrix(matrix, target):
	rows = len(matrix)
	for row in range(rows):
		print(row)
		if matrix[row][0] > target:
			continue
		elif matrix[row][len(matrix[row])-1] < target:
			continue
		else:
			for col in range(len(matrix[row])):
				print(row,col)
				if matrix[row][col] == target:
					return [row,col]
	return [-1, -1]


# O(n+m) - time
# O(1) - space
def searchInSortedMatrix(matrix, target):
	rows = len(matrix)
	row_idx = col_idx = 0
	while row_idx < rows:
		if matrix[row_idx][col_idx] == target:
			return [row_idx,col_idx]
		if col_idx == len(matrix[row_idx])-1:
			col_idx = 0
			row_idx += 1
		else:
			col_idx += 1
	return [-1, -1]