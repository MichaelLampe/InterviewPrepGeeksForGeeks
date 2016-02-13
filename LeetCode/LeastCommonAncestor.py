# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

def lowestCommonAncestor(root, p, q):
	"""
	:type root: TreeNode
	:type p: TreeNode
	:type q: TreeNode
	:rtype: TreeNode
	"""
	if root is None:
		return None

	if root is p:
		return p

	if root is q:
		return q

	check_left = lowestCommonAncestor(root.left, p, q)
	check_right = lowestCommonAncestor(root.right, p, q)

	# Ancestor
	if (check_left is not None) and (check_right is not None):
		return root
	else:
		if check_left is not None:
			return check_left
		elif check_right is not None:
			return check_right
		else:
			return None

root = TreeNode(1)
root.right = TreeNode(2)
root.left = TreeNode(3)
root.right.right = TreeNode(4)
root.right.left = TreeNode(5)
root.left.right = TreeNode(6)
root.left.left = TreeNode(7)

assert lowestCommonAncestor(root, root.right, root.right.right).val == 2
print "Finished without assertion errors"
