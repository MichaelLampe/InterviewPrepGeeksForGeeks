def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    if m == 0:
        for i in xrange(len(nums2)):
            nums1[i] = nums2[i]
        return

    if n == 0:
        return

    i1 = m - 1
    i2 = n - 1

    while (i1 >= 0) and (i2 >= 0):
        if nums1[i1] >= nums2[i2]:
            nums1[i1 + i2 + 1] = nums1[i1]
            i1 -= 1
        else:
            nums1[i1 + i2 + 1] = nums2[i2]
            i2 -= 1

    while i2 >= 0:
        nums1[i2] = nums2[i2]
        i2 -= 1

x = [1, 0]

merge(x, 1, [2], 1)

assert x == [1, 2]
print "Done w/o assertion error"