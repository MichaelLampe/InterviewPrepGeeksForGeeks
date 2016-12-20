# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


def preorderTraversal(root):
	"""
	:type root: TreeNode
	:rtype: List[int]
	"""
	if root is None:
		return []

	return_list = []
	if root.left is not None:
		return_list.extend(preorderTraversal(root.left))

	return_list.extend([root.val])

	if root.right is not None:
		return_list.extend(preorderTraversal(root.right))

	return return_list


r = TreeNode(1)
r.right = TreeNode(2)
r.right.left = TreeNode(3)

print preorderTraversal(r)