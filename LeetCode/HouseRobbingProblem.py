def rob(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	memorize = [0] * (len(nums) + 1)
	if len(nums) == 0:
		return 0
	elif len(nums) == 1:
		return nums[0]
	memorize[0] = 0
	memorize[1] = nums[0]

	for i in xrange(2, len(nums) + 1):
		# Either the sum stays the same because we want the last element
		# Or it increases because we took the element two prior and the current element
		memorize[i] = max(memorize[i - 1], (memorize[i - 2] + nums[i - 1]))

	return memorize[len(nums)]

assert rob([5, 5, 5]) == 10
assert rob([100]) == 100
assert rob([]) == 0
print "Finished w/o assertion error"
