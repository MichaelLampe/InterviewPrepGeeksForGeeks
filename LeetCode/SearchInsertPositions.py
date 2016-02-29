def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if nums[0] >= target:
        return 0

    for index in xrange(1, len(nums)):
        if nums[index] == target:
            return index
        if nums[index-1] < target and nums[index] > target:
            return index

    return len(nums)