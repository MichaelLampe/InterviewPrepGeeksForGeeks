def singleNumber(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	number = 0
	for n in nums:
		number = number ^ n
	return number


assert singleNumber([1, 2, 2, 2, 2, 1, 3]) == 3
