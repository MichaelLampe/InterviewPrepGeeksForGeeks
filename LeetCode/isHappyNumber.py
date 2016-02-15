def isHappy(n):
	"""
	:type n: int
	:rtype: bool
	"""
	if n == 1:
		return True
	seen_before = []

	value = n

	while value != 1:
		if value in seen_before:
			return False
		seen_before.append(value)

		total = 0
		for d in [int(d) for d in str(value)]:
			total += d ** 2
		value = total

	return True

assert isHappy(7) == True
assert isHappy(8) == False
assert isHappy(9) == False
assert isHappy(10) == True
print "Finished without assertion errors"

