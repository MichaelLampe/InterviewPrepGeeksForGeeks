def singleNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    track = dict()
    for n in nums:
        if track.get(n) is None:
            track[n] = 1
        else:
            track[n] += 1

    for k in track.keys():
        if track[k] == 1:
            return k