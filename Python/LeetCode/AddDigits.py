def addDigits(num):
	if num < 10:
		return num

	return addDigits(sumOfDigits(num))


def sumOfDigits(num):
	digits = [int(i) for i in str(num)]
	return sum(digits)


def addDigitsConstantTime(num):
	if num < 0:
		raise ValueError("Number should not be negative")
	elif num == 0:
		return 0
	return num - 9 * ((num - 1) / 9)

# Test a bunch of cases
for x in xrange(0, 10001):
	if addDigits(x) == addDigitsConstantTime(x):
		continue
	else:
		print "Broke"
		break

