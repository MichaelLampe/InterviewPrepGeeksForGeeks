def isPowerOfTwo(n):
	"""
	:type n: int
	:rtype: bool
	"""
	if n <= 0:
		return False
	while n % 2 == 0:
		n /= 2
	return n == 1


# This is actually slower than the serial division on LeetCode
def isPowerOfTwoBitwise(n):
	if n <= 0:
		return False
	return n & (n - 1) == 0


assert isPowerOfTwo(2) == True
assert isPowerOfTwo(8) == True
assert isPowerOfTwo(9) == False
print "Finished checking serial division without assertion error"
assert isPowerOfTwoBitwise(2) == True
assert isPowerOfTwoBitwise(8) == True
assert isPowerOfTwoBitwise(9) == False
print "Finished checking bitwise without assertion error"
