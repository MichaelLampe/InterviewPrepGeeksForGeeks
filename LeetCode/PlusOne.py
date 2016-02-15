def plusOne(digits):
	"""
	:type digits: List[int]
	:rtype: List[int]
	"""
	# Start at tail
	if digits[-1] + 1 < 10:
		digits[-1] += 1
		return digits
	if digits == [9]:
		return [1, 0]
	else:
		carry = 1
		index = 1
		while carry > 0:
			if index > len(digits):
				digits[0] = 0
				digits.insert(0, 1)
				return digits
			digits[-index] += carry
			# Check if we still have carry
			if digits[-index] > 9:
				digits[-index] = 0
				carry = 1
			else:
				return digits

			index += 1

	return digits


assert plusOne([1, 2, 3, 4, 9]) == [1, 2, 3, 5, 0]
assert plusOne([9]) == [1, 0]
assert plusOne([1, 0]) == [1, 1]
assert plusOne([9, 9]) == [1, 0, 0]
assert plusOne([8, 9, 9, 9]) == [9, 0, 0, 0]
print "Finished without assertion error"
