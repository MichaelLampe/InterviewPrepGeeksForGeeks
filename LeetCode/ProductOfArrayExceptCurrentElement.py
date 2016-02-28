def productExceptSelf(nums):
	"""
	:type nums: List[int]
	:rtype: List[int]
	"""
	fwd_pos = [0] * len(nums)
	rev_pos = [0] * len(nums)

	fwd_pos[0] = 1
	rev_pos[-1] = 1

	for i in xrange(1, len(nums)):
		fwd_pos[i] = nums[i - 1] * fwd_pos[i - 1]

	for i in xrange(len(nums) - 2, -1, -1):
		rev_pos[i] = nums[i + 1] * rev_pos[i + 1]

	ret_arr = [0] * len(nums)
	for i in xrange(0, len(nums)):
		ret_arr[i] = fwd_pos[i] * rev_pos[i]

	return ret_arr


n = [1, 2, 3, 4]
assert productExceptSelf(n) == [24, 12, 8, 6]
