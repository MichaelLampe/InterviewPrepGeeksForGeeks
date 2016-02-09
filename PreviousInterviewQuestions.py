import math


def sum_dif_of_binary_pairs(input_numbers):
	"""
	Found on geeks for geeks as a past google interview question
	Implementation is my own

	Given an integer array of n integers, find sum of bit differences in all pairs that can be formed from array elements.
	Bit difference of a pair (x, y) is count of different bits at same positions in binary representations of x and y.
	For example, bit difference for 2 and 7 is 2.
	Binary representation of 2 is 010 and 7 is 111 ( first and last bits differ in two numbers).
	"""
	max_int_length = 0
	binary_numbers = []

	# N operations
	for number in input_numbers:
		binary_version = bin(number)
		binary_version = binary_version[2:len(binary_version)]
		binary_numbers.append(binary_version)
		if len(binary_version) > max_int_length:
			max_int_length = len(binary_version)

	# Standardize length, N operations
	for number_index in xrange(len(binary_numbers)):
		binary_numbers[number_index] = binary_numbers[number_index].zfill(max_int_length)


	# c*N iterations where c is max_int_length which is not that big.
	# That means that it is O(N)
	comb = 0
	for bit in xrange(max_int_length):
		number_of_ones = 0
		number_of_zeros = 0
		for number in binary_numbers:
			# Exception is a good first hack, could also standardize bin length
			if int(number[bit]) == 1:
				number_of_ones += 1
			else:
				number_of_zeros += 1

		# Breaks into a combinations calculation w/ a defined formula
		comb += number_of_ones * number_of_zeros * 2

	return comb


def determine_if_multiple_of_5_power_n(number):
	log_of = math.log(number, 5.0)
	return log_of.is_integer()