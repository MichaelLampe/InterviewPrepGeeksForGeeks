def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if l1 is None:
        return l2
    elif l2 is None:
        return l1

    if (l1.val <= l2.val):
        new_list_head = l1
        current_node = l1
        l1 = l1.next
    else:
        new_list_head = l2
        current_node = l2
        l2 = l2.next
    # Put together as many as possible initially
    while (l1 is not None) and (l2 is not None):
        if l1.val <= l2.val:
            current_node.next = l1
            l1 = l1.next
        else:
            current_node.next = l2
            l2 = l2.next
        current_node = current_node.next

    # Append whatever the leftovers are
    if l1 is not None:
        current_node.next = l1
    else:
        current_node.next = l2

    return new_list_head