from collections import deque

class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue_in = deque()
        self.queue_out = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue_in.appendleft(x)

    def pop(self):
        """
        :rtype: nothing
        """
        while len(self.queue_in) > 1:
            self.queue_out.appendleft(self.queue_in.pop())
        # Last element is top of stack
        popped_node = self.queue_in.pop()

        while len(self.queue_out) > 0:
            self.queue_in.appendleft(self.queue_out.pop())

        return popped_node

    def top(self):
        """
        :rtype: int
        """
        while len(self.queue_in) > 1:
            self.queue_out.appendleft(self.queue_in.pop())

        show_node = self.queue_in.pop()

        while len(self.queue_out) > 0:
            self.queue_in.appendleft(self.queue_out.pop())
        self.queue_in.appendleft(show_node)

        return show_node

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue_in) == 0