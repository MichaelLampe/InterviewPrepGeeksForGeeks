def isSymmetric(root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return symmetricHelper(root.left, root.right)


def symmetricHelper(left_node, right_node):
    if left_node is None:
        return right_node is None
    if right_node is None:
        return left_node is None

    if left_node.val != right_node.val:
        return False
    else:
        left = symmetricHelper(left_node.left, right_node.right)
        right = symmetricHelper(left_node.right, right_node.left)
        return left and right
