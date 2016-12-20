def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    last_element = None
    last_element_pointer = 0
    for element in nums:
        if element == last_element:
            continue
        else:
            last_element = element
            nums[last_element_pointer] = element
            last_element_pointer += 1

    return last_element_pointer

assert removeDuplicates([1, 2, 2, 2, 2, 2, 2, 2]) == 2
assert removeDuplicates([]) == 0
assert removeDuplicates([1]) == 1
print "Finished w/o assertion error"
