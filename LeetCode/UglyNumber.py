def isUgly(num):
	"""
	:type num: int
	:rtype: bool
	"""
	if num == 0:
		return False
	# Divide a lot
	while (num % 2 == 0) or (num % 3 == 0) or (num % 5 == 0):
		if num % 2 == 0:
			num /= 2
		elif num % 3 == 0:
			num /= 3
		else:
			num /= 5

	# Check if any other prime factors exist
	return num == 1


# Ugly number has only 2, 3, 5 as factors
test_cases = [(2, True),
              (3, True),
              (4, True),
              (5, True),
              (6, True),
              (7, False),
              (0, False),
              (-1, False)]

for case in test_cases:s
	assert isUgly(case[0]) == case[1]
print "Finished without assertion error"