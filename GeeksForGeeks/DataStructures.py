
# Python heap API relies on
# 1) Heappush
# 2) Heappop
# It just kinda knows when you give it an array where to put the items if you iterate over them for O(N)
from heapq import (heappush, heappop)

given_array = [1, 2, 3, 4, 5, 6, 7]
heap = []

# Min heap
for item in given_array:
	heappush(heap, item)
print heap

# Max heap we just invert the input
heap = []
for item in given_array:
	heappush(heap, -item)
print heap


