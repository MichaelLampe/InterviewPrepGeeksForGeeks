def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    current_sum = nums[0]
    _max = nums[0]

    # keep track of the max sum as a position
    # and the sum of where we are now
    for index in xrange(1, len(nums)):
        current_sum = max(current_sum + nums[index], nums[index])
        _max = max(current_sum, _max)

    return _max
