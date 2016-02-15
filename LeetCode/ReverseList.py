# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_list(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        new_head = ListNode(head.val)
        current_node = head.next
        while current_node is not None:
            # Create new node
            copy_current = ListNode(current_node.val)

            # Set the next node as the previous head and switch to being the head
            copy_current.next = new_head
            new_head = copy_current

            # Move the loop forward
            current_node = current_node.next
        return new_head
