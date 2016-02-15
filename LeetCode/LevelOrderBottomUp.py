from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


def levelOrderBottom(root):
	"""
	:type root: TreeNode
	:rtype: List[List[int]]
	"""
	if root is None:
		return []

	return_list = []

	current_nodes = deque()
	next_nodes = deque()
	current_nodes.appendleft(root)

	current_level_list = []
	# Iterate through current level adding values to list and new nodes to the next node queue
	while len(current_nodes) > 0:
		node = current_nodes.pop()

		# Add the node's children to the next nodes
		if node.left is not None:
			next_nodes.appendleft(node.left)
		if node.right is not None:
			next_nodes.appendleft(node.right)

		current_level_list.append(node.val)

		# When our current queue is empty
		if len(current_nodes) == 0:
			return_list.append(current_level_list)

			# If there are next nodes, reset stuff
			if len(next_nodes) > 0:
				current_nodes = next_nodes
				next_nodes = deque()
				current_level_list = []
			else:
				# We done
				break

	# Reverse list
	return return_list[::-1]


root = TreeNode(1)
root.right = TreeNode(3)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.right.right = TreeNode(7)
root.right.left = TreeNode(15)
x = levelOrderBottom(root)

assert x == [[4, 15, 7], [2, 3], [1]]
print "Passes all assertions"
