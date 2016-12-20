def deleteDuplicates(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        previous_node = head
        node = head.next
        while node is not None:
            # Remove
            if node.val <= previous_node.val:
                previous_node.next = node.next
            else:
                previous_node = node
            node = node.next

        return head
