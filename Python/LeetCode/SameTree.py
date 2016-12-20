# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def isSameTree(p, q):
	"""
	:type p: TreeNode
	:type q: TreeNode
	:rtype: bool
	"""
	if p is None and q is not None:
		return False
	elif p is not None and q is None:
		return False
	elif p is None and q is None:
		return True

	if p.val != q.val:
		return False
	else:
		left = isSameTree(p.left, q.left)
		right = isSameTree(p.right, q.right)
		return left and right

tree_one_root = TreeNode(1)
tree_one_root.left = TreeNode(2)

tree_two_root = TreeNode(1)
tree_two_root.left = TreeNode(2)

print isSameTree(tree_one_root, tree_two_root)

tree_one_root.right = TreeNode(3)
print isSameTree(tree_one_root, tree_two_root)