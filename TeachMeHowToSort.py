from numpy import median

def quicksort(array):
	less = []
	equal = []
	greater = []

	if len(array) > 1:
		# Picking a pivot is fun.
		pivot = array[0]

		for val in array:
			if val < pivot:
				less.append(val)
			elif val > pivot:
				greater.append(val)
			else:
				equal.append(val)

		return quicksort(less) + equal + quicksort(greater)
	else:
		return array

def quicksort_median_pivot(array):
	less = []
	equal = []
	greater = []

	if len(array) > 1:
		# Picking a pivot is fun.
		pivot = median(array)

		for val in array:
			if val < pivot:
				less.append(val)
			elif val > pivot:
				greater.append(val)
			else:
				equal.append(val)

		return quicksort(less) + equal + quicksort(greater)
	else:
		return array

def mergesort(unsorted_array):
	# Base case
	if len(unsorted_array) < 2:
		return unsorted_array

	def merge_two_sorted_arrays(l_array, r_array):
		result_array_length = len(l_array) + len(r_array)
		result_array = [None] * result_array_length

		left_array_index = 0
		right_array_index = 0
		result_array_index = 0

		# Place the initial results
		while (left_array_index < len(l_array)) and (right_array_index < len(r_array)):
			if l_array[left_array_index] <= r_array[right_array_index]:
				result_array[result_array_index] = l_array[left_array_index]
				left_array_index += 1
			else:
				result_array[result_array_index] = r_array[right_array_index]
				right_array_index += 1
			result_array_index += 1
		# Deal with any leftovers

		# On the left
		while left_array_index < len(l_array):
			result_array[result_array_index] = l_array[left_array_index]
			left_array_index += 1
			result_array_index += 1

		# On the right
		while right_array_index < len(r_array):
			result_array[result_array_index] = r_array[right_array_index]
			right_array_index += 1
			result_array_index += 1
		return result_array

	split_index = len(unsorted_array)/2
	left_array = mergesort(unsorted_array[0:split_index])
	right_array = mergesort(unsorted_array[split_index:len(unsorted_array)])
	sorted_array = merge_two_sorted_arrays(left_array, right_array)

	return sorted_array