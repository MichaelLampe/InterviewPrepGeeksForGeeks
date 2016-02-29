def connect(self, root):
    """
    :type root: TreeLinkNode
    :rtype: nothing
    """
    from collections import deque

    if root is None:
        return

    current_nodes = deque()
    next_nodes = deque()
    current_nodes.appendleft(root)

    while len(current_nodes) > 0:
        current_node = current_nodes.pop()
        if current_node.left is not None:
            next_nodes.appendleft(current_node.left)
        if current_node.right is not None:
            next_nodes.appendleft(current_node.right)

        if len(current_nodes) > 0:
            # Add point to next
            current_node.next = current_nodes.pop()
            current_nodes.append(current_node.next)
        else:
            current_node.next = None
            current_nodes, next_nodes = next_nodes, deque()