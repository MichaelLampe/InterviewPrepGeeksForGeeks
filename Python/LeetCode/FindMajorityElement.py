def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # This performs pretty fast, but I think the worst case complexity is N^2
    # N/2 elements at the most, N time to count each time.
    #
    # Could also use a hashmap to hash the numbers as we go to track their values and then find the max
    # Which is N + N or O(N)
    majority = len(nums)/2
    unique_elements = set(nums)
    for e in unique_elements:
        current_count = nums.count(e)
        if current_count > majority:
            return e

assert majorityElement([2, 2, 2, 2, 1]) == 2
assert  majorityElement([3, 0, 0, 0, 3]) == 0
print "Finished without assertion errors"