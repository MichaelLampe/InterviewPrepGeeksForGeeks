def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    unique = set(nums)
    return len(unique) != len(nums)

assert containsDuplicate([1, 1]) == True
assert containsDuplicate([1, 2]) == False
print "Finished without assertion errors"