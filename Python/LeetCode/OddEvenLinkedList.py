# Inplace moves odd nodes to front and even nodes to back
def oddEvenList(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head


        odd_head = head
        even_head = head.next

        # Keep track of where we are so we know which one to append it to
        count = 1
        # The tail of the odd nodes will be used to connect the even and odds
        last_odd_node = odd_head
        last_even_node = even_head
        if head.next is not None:
            iteration_node = head.next.next
        else:
            iteration_node = None
        while iteration_node is not None:
            # Even case
            next_node = iteration_node.next
            if count % 2 == 0:
                last_even_node.next = iteration_node
                last_even_node = iteration_node
            else:
                last_odd_node.next = iteration_node
                last_odd_node = iteration_node
            iteration_node = next_node
            count += 1

        # Disconnect tail from previous next
        if last_even_node is not None:
            last_even_node.next = None
        # Connect the two again
        last_odd_node.next = even_head
        return odd_head