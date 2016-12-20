def singleNumber(nums):
	"""
	:type nums: List[int]
	:rtype: List[int]
	"""
	counts = {}
	for num in nums:
		if counts.get(num) is None:
			counts[num] = 1
		else:
			counts[num] += 1

	single_numbers = []
	for key in counts.keys():
		if counts[key] == 1:
			single_numbers.append(key)
	if len(single_numbers) == 0:
		return [0, 0]

	return single_numbers


"""
I coded the above without looking at anything, but I wanted to get the bitwise solution so here is my coding of that.

I get that you save at most N/2 space [O(N)].

The unique bit trick is pretty slick as well, but I wouldn't have gotten it alone.
"""
def singleNumberBitwise(nums):
	result = 0
	for num in nums:
		result ^= num

	unique_bit = result & (~result + 1)

	number_one, number_two = 0, 0

	for num in nums:
		if num & unique_bit:
			number_one ^= num
		else:
			number_two ^= num

	return [number_one, number_two]

array = [1, 3]
assert singleNumberBitwise(array) == singleNumber(array) or singleNumberBitwise(array)[::-1] == singleNumber(array)
print "Passed all assertion tests"