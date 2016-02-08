from collections import deque


# Define a graph
class Graph:
    def __init__(self):
        self.graph = dict()

    def add_node(self, node_name):
        # Edges are stored as a list
        self.graph[node_name] = list()

    def add_edge(self, node_1, node_2):
        if self.graph.get(node_1) is None:
            self.add_node(node_1)

        if self.graph.get(node_2) is None:
            self.add_node(node_2)

        if node_2 not in self.graph[node_1]:
            self.graph[node_1].append(node_2)

        if node_1 not in self.graph[node_2]:
            self.graph[node_2].append(node_1)

    def breadth_first_search(self, start_node, looking_for_node):
        """
        start_node <- where our algorithm will start looking
        looking_for_node <- what our algorithm is looking for
        Returns true if looking for node is in graph based on bfs
        """
        print "Starting node is {0}".format(start_node)
        if start_node is looking_for_node:
            return True

        visited = list()
        visited.append(start_node)
        frontier = deque()

        for node in self.graph[start_node]:
            frontier.append(node)

        while len(frontier) > 0:
            current_node = frontier.popleft()
            visited.append(current_node)
            print "Next node looked at is {0}".format(current_node)

            if current_node == looking_for_node:
                return True

            for node in self.graph[current_node]:
                if node not in visited:
                    frontier.append(node)
        return False

    def depth_first_search(self, start_node, looking_for_node):
        """
        start_node <- where our algorithm will start looking
        looking_for_node <- what our algorithm is looking for
        Returns true if looking for node is in graph based on bfs
        """
        print "Starting node is {0}".format(start_node)
        if start_node is looking_for_node:
            return True

        visited = list()
        visited.append(start_node)
        frontier = deque()

        for node in self.graph[start_node]:
            frontier.append(node)

        while len(frontier) > 0:
            current_node = frontier.pop()
            visited.append(current_node)
            print "Next node looked at is {0}".format(current_node)

            if current_node == looking_for_node:
                return True

            for node in self.graph[current_node]:
                if node not in visited:
                    frontier.append(node)
        return False

    def depth_first_traversal(self, current_node, visited=None):
        print "Visiting the node {0}".format(current_node)
        if visited is None:
            visited = [current_node]
        else:
            visited.append(current_node)

        for node in self.graph[current_node]:
            if node not in visited:
                self.depth_first_traversal(node, visited)
