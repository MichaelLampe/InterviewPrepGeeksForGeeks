def hasPathSum(root, sum):
	"""
	:type root: TreeNode
	:type sum: int
	:rtype: bool
	"""
	if root is None:
		return False
	if root.right is None and root.left is None:
		return root.val == sum

	if root.right is not None:
		if pathSumHelper(root.right, root.val, sum):
			return True
	if root.left is not None:
		if pathSumHelper(root.left, root.val, sum):
			return True

	return False


def pathSumHelper(root, currentSum, lookingForSum):
	currentSum += root.val

	# If leaf node
	if root.left is None and root.right is None:
		return currentSum == lookingForSum

	if root.left is not None:
		if pathSumHelper(root.left, currentSum, lookingForSum):
			return True

	if root.right is not None:
		if pathSumHelper(root.right, currentSum, lookingForSum):
			return True

	return False
