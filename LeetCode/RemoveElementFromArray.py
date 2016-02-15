def removeElement(nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            if nums[0] == val:
                return 0
            else:
                return 1

        good_value_pointer = 0

        for index in xrange(len(nums)):
            if nums[index] != val:
                nums[good_value_pointer] = nums[index]
                good_value_pointer += 1

        return good_value_pointer

assert removeElement([1, 2, 3, 4, 5], 0) == 5
assert removeElement([1, 2, 3, 3, 3], 3) == 2
assert removeElement([], 0) == 0
assert removeElement([1], 0) == 1
assert removeElement([1], 1) == 0
print "Finished without assertion errors"