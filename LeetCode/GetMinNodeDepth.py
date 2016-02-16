def minDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root is None:
        return 0

    if (root.left is None) and (root.right is None):
        return 1

    if (root.left is None) or (root.right is None):
        if root.left is None:
            return minDepth(root.right) + 1
        if root.right is None:
            return minDepth(root.left) + 1

    return min(minDepth(root.right) + 1, minDepth(root.left) + 1)