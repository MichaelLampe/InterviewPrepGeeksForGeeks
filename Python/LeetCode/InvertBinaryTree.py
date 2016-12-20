# Definition for a binary tree node.
from collections import deque

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

def print_tree_node(root):
	# Bfs root node printing
	queue = deque()
	queue.append(root)
	print_string = ""
	while len(queue) > 0:
		current_node = queue.popleft()
		if print_string != "":
			print_string += " - "
		print_string += str(current_node.val)
		if current_node.left is not None:
			queue.append(current_node.left)
		if current_node.right is not None:
			queue.append(current_node.right)
	return print_string


def invertTree(root):
	"""
	:type root: TreeNode
	:rtype: TreeNode
	"""
	if root is None:
		return root

	left = root.left
	right = root.right
	root.right = invertTree(left)
	root.left = invertTree(right)
	return root

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print print_tree_node(root)
invertTree(root)
print print_tree_node(root)


