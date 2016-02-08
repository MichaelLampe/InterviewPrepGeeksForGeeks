# Implement various algorithms in python
#http://www.geeksforgeeks.org/top-10-algorithms-in-interview-questions/



"""
Graph Theory
"""
from GraphTheory import Graph
my_graph = Graph()

my_graph.add_edge("A", "B")
my_graph.add_edge("A", "C")
my_graph.add_edge("A", "D")
my_graph.add_edge("B", "E")
my_graph.add_edge("D", "F")


print my_graph.breadth_first_search("A", "E")      # 1
print my_graph.depth_first_search("A", "F")        # 2
print my_graph.depth_first_traversal("A")          # 2
