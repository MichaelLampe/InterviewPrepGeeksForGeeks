class LinkedList:
    class Node:
        def __init__(self, data, next_node=None):
            self.data = data
            self.next_node_pointer = next_node

        def set_next_node(self, node):
            self.next_node_pointer = node

        def set_next_node_none(self):
            self.set_next_node(None)

    def __init__(self):
        self.head = None

    def add_node(self, data):
        if self.head is None:
            self.head = self.Node(data)
        else:
            tail_node = self.get_tail_node()
            tail_node.set_next_node(self.Node(data))

    def add_node_sorted(self, data):
        if self.head is None:
            self.head = self.Node(data)
        else:
            if self.head.data <= data:
                previous_node = self.head
                current_node = self.head.next_node_pointer
                while current_node.data <= data:
                    previous_node = current_node
                    current_node = current_node.next_node_pointer
                previous_node.next_node_pointer = self.Node(data)
                previous_node.next_node_pointer.next_node_pointer = current_node

            else:
                new_node = self.Node(data)
                new_node.next_node_pointer = self.head
                self.head = new_node

    def remove_node(self, data):
        if self.head is None:
            return
        else:
            current_node = self.head
            if current_node == data:
                removed_node = self.head
                self.head = current_node.next_node_pointer
                removed_node.next_node_pointer = None
                return removed_node
            else:
                previous_node = self.head
                while current_node is not None:
                    if current_node.data == data:
                        removed_node = current_node
                        previous_node.next_node_pointer = current_node.next_node_pointer
                        removed_node.next_node_pointer = None
                        return removed_node
                    else:
                        previous_node = current_node
                        current_node = current_node.next_node_pointer
                return None

    def get_tail_node(self):
        if self.head is None:
            return None
        else:
            previous_parent = self.head
            next_node = self.head.next_node_pointer
            while next_node is not None:
                previous_parent = next_node
                next_node = next_node.next_node_pointer
            return previous_parent

    def linked_list_to_string(self):
        output = ""
        current_node = self.head
        while current_node is not None:
            if output != "":
                output += "-"
            output += str(current_node.data)
            current_node = current_node.next_node_pointer
        return output