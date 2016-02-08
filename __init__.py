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

print my_graph.breadth_first_search("A", "E")
