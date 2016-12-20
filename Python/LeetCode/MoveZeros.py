import random
import time


# Better solution when we have few zeros
def moveZeroes(nums):
	"""
	:type nums: List[int]
	:rtype: void Do not return anything, modify nums in-place instead.
	"""
	for index in xrange(len(nums) - 1, -1, -1):
		if nums[index] == 0:
			nums.append(nums.pop(index))


# Better solution when we have lots of zeros
def moveZerosLinearTime(nums):
	non_zeros = 0

	# Place all the nonzeros at the front
	for index in xrange(len(nums)):
		if nums[index] != 0:
			nums[non_zeros] = nums[index]
			non_zeros += 1

	# Append nonzeros
	for index in xrange(non_zeros, len(nums)):
		nums[index] = 0


input_array = [1, 0, 3, 5, 1, 0, 10]
print input_array
moveZeroes(input_array)
print input_array

input_array = [1, 0, 3, 5, 1, 0, 10]
print input_array
moveZerosLinearTime(input_array)
print input_array

# Time difference when there are very few zeros, so the best case for the original function
# The nonlinear time worst case function is about 3x faster
input_array = random.sample(xrange(10000000), 100000)
input_array[50] = 0
input_array[500] = 0
a = input_array
b = input_array

s = time.clock()
moveZeroes(a)
print time.clock() - s
s = time.clock()
moveZerosLinearTime(b)
print time.clock() - s


# Time difference when we have a lot of zeros
# The linear time function is about 200x faster
input_array = [0]*100000
input_array[50] = 5
input_array[5000] = 10
a = input_array
b = input_array

s = time.clock()
moveZeroes(a)
print time.clock() - s
s = time.clock()
moveZerosLinearTime(b)
print time.clock() - s

