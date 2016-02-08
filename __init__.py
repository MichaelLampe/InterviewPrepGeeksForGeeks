# Implement various algorithms in python
# http://www.geeksforgeeks.org/top-10-algorithms-in-interview-questions/



"""
Graph Theory
"""
print "GRAPH THEORY"
from GraphTheory import Graph
my_graph = Graph()

my_graph.add_edge("A", "B")
my_graph.add_edge("A", "C")
my_graph.add_edge("A", "D")
my_graph.add_edge("B", "E")
my_graph.add_edge("D", "F")


print my_graph.breadth_first_search("A", "E")      # 1
print my_graph.depth_first_search("A", "F")        # 2
my_graph.depth_first_traversal("A")                # 2


"""
Linked Lists
"""
print "\n\n\nLINKED LISTS"
from LinkedLists import LinkedList
my_linked_list = LinkedList()

my_linked_list.add_node("A")
my_linked_list.add_node("B")
my_linked_list.add_node("D")
my_linked_list.add_node_sorted("C")                 # 1

print my_linked_list.linked_list_to_string()
print my_linked_list.remove_node("C").data
print my_linked_list.linked_list_to_string()
