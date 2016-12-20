def isPowerOfThree(n):
    """
    :type n: int
    :rtype: bool
    """
    if n <= 0:
        return False
    while n % 3 == 0:
        n /= 3
    return n == 1

assert isPowerOfThree(3) == True
assert isPowerOfThree(8) == False
assert isPowerOfThree(27) == True
print "Finished without assertion error"
