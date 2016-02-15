from collections import deque

# This version has fast insertion, but slow lookup.
# Could implement with more focus on fast lookup by having the queues interact more dynamically.
class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.first_stack = deque()
        self.second_stack = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.first_stack.appendleft(x)


    def pop(self):
        """
        :rtype: nothing
        """
        # Unload first stack into second stack
        while len(self.first_stack) > 0:
            self.second_stack.appendleft(self.first_stack.popleft())
        return_value = self.second_stack.popleft()

        # Reload the first stack
        while len(self.second_stack) > 0:
            self.first_stack.appendleft(self.second_stack.popleft())

        return return_value


    def peek(self):
        """
        :rtype: int
        """
        while len(self.first_stack) > 0:
            self.second_stack.appendleft(self.first_stack.popleft())
        return_value = self.second_stack.popleft()

        # Readd element
        self.second_stack.appendleft(return_value)
        # Reload the first stack
        while len(self.second_stack) > 0:
            self.first_stack.appendleft(self.second_stack.popleft())

        return return_value

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.first_stack) == 0