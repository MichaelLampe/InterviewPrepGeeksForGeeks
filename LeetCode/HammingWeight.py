def hammingWeight(n):
    """
    :type n: int
    :rtype: int
    """
    # Basic solution where we just count the 1s
    binary_rep = bin(n)[2:]
    count = 0
    for c in binary_rep:
        if int(c) == 1:
            count += 1
    return count

assert hammingWeight(5) == 2
assert hammingWeight(0) == 0

print "Finished without assertion errors"