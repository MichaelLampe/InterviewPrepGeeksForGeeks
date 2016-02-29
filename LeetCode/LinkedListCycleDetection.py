def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    # Slow and fast pointer method
    slow = head
    fast = head

    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False