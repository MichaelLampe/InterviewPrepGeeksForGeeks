def isBalanced(root):
	"""
	:type root: TreeNode
	:rtype: bool
	"""
	if root is None:
		return True

	# -1 is our signal value for unbalanced
	return isBalancedHelper(root) != -1


def isBalancedHelper(root):
	if root is None:
		return 0

	# Use -1 as a not-balanced indictator

	# Check to see if left root is balanced
	left_balanced = isBalancedHelper(root.left)
	if left_balanced == -1:
		return -1

	# Check to see if right root is balanced
	right_balanced = isBalancedHelper(root.right)
	if right_balanced == -1:
		return -1

	# Check the difference between to see if not balanced
	if abs(right_balanced - left_balanced) > 1:
		return -1
	else:
		# Otherwise we want to return the deepest node
		return max(right_balanced, left_balanced) + 1
