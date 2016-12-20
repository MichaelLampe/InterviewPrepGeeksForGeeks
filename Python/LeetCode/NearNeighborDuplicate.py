def containsNearbyDuplicate(nums, k):
	"""
	:type nums: List[int]
	:type k: int
	:rtype: bool
	"""
	local_numbers = set()
	for index in xrange(len(nums)):
		if nums[index] in local_numbers:
			return True
		else:
			local_numbers.add(nums[index])

		if index >= k:
			local_numbers.remove(nums[index - k])

	return False


s = [1, 2, 1, 4, 5, 6]
assert containsNearbyDuplicate(s, 1) == False
assert containsNearbyDuplicate(s, 2) == True
