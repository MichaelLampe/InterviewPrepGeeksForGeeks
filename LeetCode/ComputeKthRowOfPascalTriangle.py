from math import factorial
def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    # Compute factorial
    return_list = list()
    for i in xrange(rowIndex+1):
        value = factorial(rowIndex)/(factorial(rowIndex - i)*factorial(i))
        return_list.append(value)
    return return_list

assert getRow(0) == [1]
assert getRow(1) == [1, 1]
assert getRow(2) == [1, 2, 1]
assert getRow(3) == [1, 3, 3, 1]
print "Finished without assertion error"