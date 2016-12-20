def missingNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0

        # Just find the nonduplicate
        nums = nums + range(len(nums)+1)
        for num in nums:
            result = result ^ num
        return result