def reverseBits(n):
	"""
	:type n: int
	:rtype: int
	"""

	# Convert input to 32 bit binary
	binary_number = bin(n)[2:].zfill(32)

	# Reverse
	binary_number = binary_number[::-1]

	# Return as an int
	return int(binary_number, 2)
