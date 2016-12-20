# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None


def printNodes(head):
	node = head
	node_string = ""
	while node is not None:
		if node_string != "":
			node_string += " - "
		node_string += str(node.val)
		node = node.next
	return node_string


def deleteNode(node):
	"""
	:type node: ListNode
	:rtype: void Do not return anything, modify node in-place instead.
	"""
	next_node = node.next
	if next_node is not None:
		node.val = next_node.val
		node.next = next_node.next


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print printNodes(head)
deleteNode(head.next.next)
print printNodes(head)
