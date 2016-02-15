from collections import deque

def levelOrder(root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        current_queue = deque()
        next_queue = deque()
        current_queue.appendleft(root)

        return_list = list()

        current_sublist = list()
        while len(current_queue) > 0:
            current_node = current_queue.pop()
            current_sublist.append(current_node.val)

            if current_node.left is not None:
                next_queue.appendleft(current_node.left)
            if current_node.right is not None:
                next_queue.appendleft(current_node.right)

            if len(current_queue) == 0:
                return_list.append(current_sublist)
                current_sublist = list()
                current_queue = next_queue
                next_queue = deque()

        return return_list