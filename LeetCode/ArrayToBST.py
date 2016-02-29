# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


def sortedArrayToBST(nums):
	"""
	:type nums: List[int]
	:rtype: TreeNode
	"""
	if len(nums) == 0:
		return None
	if len(nums) == 1:
		print nums[0]
		return TreeNode(nums[0])

	median = (len(nums)-1) / 2
	print "Median"
	print nums[median]
	root = TreeNode(nums[median])

	print "Left"
	root.left = sortedArrayToBST(nums[0:median])
	print "Right"
	root.right = sortedArrayToBST(nums[median+1:len(nums)])

	return root

sortedArrayToBST([1, 2, 3, 4, 5, 6, 7, 8, 9])
