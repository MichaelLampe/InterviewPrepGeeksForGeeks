# Just a bucket sort.
# Could be faster if we did the first digit in place instead of bucketing it.


def sortColors(nums):
	"""
	:type nums: List[int]
	:rtype: void Do not return anything, modify nums in-place instead.
	"""
	buckets = [0, 0, 0]
	for num in nums:
		buckets[num] += 1

	pointer = 0
	for index in xrange(len(buckets)):
		for _ in xrange(buckets[index]):
			nums[pointer] = index
			pointer += 1
