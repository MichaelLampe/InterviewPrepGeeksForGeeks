def findMinLinearTime(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if nums[0] <= nums[-1]:
        return nums[0]

    for index in xrange(1, len(nums)):
        if nums[index-1] > nums[index]:
            return nums[index]

    return None

def findMinLogNBinarySearch(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_index = 0
        max_index = len(nums) - 1

        # Check if rotated
        if nums[0] < nums[-1]:
            return nums[0]

        while max_index != min_index:
            if max_index - min_index == 1:
                if nums[max_index] < nums[min_index]:
                    min_index = max_index
                break

            # Find middle point
            mid_point = min_index + (max_index - min_index)/2

            # Determine how to shift
            if nums[mid_point] > nums[min_index]:
                min_index = mid_point
            else:
                max_index = mid_point

        return nums[min_index]