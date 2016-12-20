from math import factorial


# Slow math way
def generate(numRows):
	"""
	:type numRows: int
	:rtype: List[List[int]]
	"""
	if numRows == 0:
		return []
	return_list = []
	for n in xrange(0, numRows):
		append_list = []
		for r in xrange(0, n + 1):
			a = factorial(n) / (factorial(n - r) * factorial(r))
			append_list.append(a)
		return_list.append(append_list)

	return return_list


print generate(1)
print generate(2)
print generate(3)
print generate(4)
print generate(5)


# A good bit faster based on list movements and not on factorials
def generatePascals(numRows):
	"""
	:type numRows: int
	:rtype: List[List[int]]
	"""
	if numRows == 0:
		return []
	if numRows == 1:
		return [[1]]
	return_list = [[1]]
	for _ in xrange(0, numRows - 1):
		last_row = return_list[-1]
		append_list = []
		append_list.append(1)
		for x in xrange(0, len(last_row) - 1):
			a = last_row[x] + last_row[x + 1]
			append_list.append(a)
		append_list.append(1)

		return_list.append(append_list)

	return return_list

print generatePascals(0)
print generatePascals(1)
print generatePascals(2)
print generatePascals(3)
print generatePascals(4)

for x in xrange(20):
	assert generatePascals(x) == generate(x)

print "Finished first 20 test cases w/o assertion error"