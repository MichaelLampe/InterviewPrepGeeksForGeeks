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

