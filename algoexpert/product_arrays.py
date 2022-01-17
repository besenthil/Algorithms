# O(n^2) - time
# O(n) - space
def arrayOfProducts_1(array):
	current_idx = 0
	other_idx = 0
	product_arr = []
	product = 1
	while(current_idx < len(array)):
		other_idx = 0
		product = 1
		while other_idx < len(array):
			if current_idx != other_idx:
				product *= array[other_idx]
			other_idx += 1
		current_idx += 1
		product_arr.append(product)
	return product_arr


# O(n) - time
# O(n) - space
def arrayOfProducts_2(array):
	left_array = []
	right_array = []
	for _ in range(len(array)):
		left_array.append(1)
		right_array.append(1)

	idx = 0
	running_product = 1
	while idx < len(array) - 1:
		running_product *= array[idx]
		left_array[idx + 1] = running_product
		idx += 1

	idx = len(array) - 1
	running_product = 1
	while idx > 0:
		running_product *= array[idx]
		right_array[idx - 1] = running_product
		idx -= 1

	print(left_array, right_array)
	return [a * b for a, b in zip(left_array, right_array)]


# O(n) - time
# O(n) - space
def arrayOfProducts_3(array):
	left_array = []
	right_array = []
	for _ in range(len(array)):
		left_array.append(1)
		right_array.append(1)

	idx = 0
	running_product = 1
	while idx < len(array) - 1:
		running_product *= array[idx]
		left_array[idx + 1] = running_product
		idx += 1

	idx = len(array) - 1
	running_product = 1
	while idx > 0:
		running_product *= array[idx]
		left_array[idx - 1] = left_array[idx - 1] * running_product
		idx -= 1
	return left_array
