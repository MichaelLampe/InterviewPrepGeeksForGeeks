class LRUCache:
	def __init__(self, capacity):
		"""
		:type capacity: int
		"""
		self.capacity = capacity

		self.cache = {}

		# Recency tracking
		self.recency_cache = {}
		self.additions_count = 0

	def get(self, key):
		"""
		:rtype: int
		"""
		if self.cache.get(key) is not None:
			self.recency_cache[key] = self.additions_count
			self.additions_count += 1
			return self.cache[key]
		else:
			return -1

	def set(self, key, value):
		"""
		:type key: int
		:type value: int
		:rtype: nothing
		"""
		if len(self.cache.keys()) >= self.capacity:
			if self.cache.get(key) is not None:
				self.cache[key] = value
				self.recency_cache[key] = self.additions_count
				self.additions_count += 1
				return
			# Get most recent thing
			least_recently_used_key = None
			furthest_number = 0
			for k in self.recency_cache.keys():
				distance = self.additions_count - self.recency_cache[k]
				if distance > furthest_number:
					furthest_number = distance
					least_recently_used_key = k

			self.cache.pop(least_recently_used_key, None)
			self.recency_cache.pop(least_recently_used_key, None)
			self.cache[key] = value
			self.recency_cache[key] = self.additions_count
			self.additions_count += 1
		else:
			self.recency_cache[key] = self.additions_count
			self.additions_count += 1
			self.cache[key] = value


class DoublyLinkedHashList:
	# Single instance of a doubly linked node
	class DoublyLinkedNode:
		def __init__(self, key, value, is_head=False, is_tail=False):
			self.key = key
			self.value = value
			self.prev_pointer = None
			self.next_pointer = None
			self.is_head = is_head
			self.is_tail = is_tail

		def get_value(self):
			return self.value

		def set_value(self, value):
			self.value = value

		def to_string(self):
			if self.is_head:
				return "[HEAD]"
			elif self.is_tail:
				return "[TAIL]"
			else:
				return "[Key: {0}, Value: {1}]".format(self.key, self.value)

	def __init__(self):
		# We track a hash and the head, that's it.
		self.hash = {}
		self.head_node = self.DoublyLinkedNode(-1, -1, is_head=True)
		self.tail_node = self.DoublyLinkedNode(-1, -1, is_tail=True)

		self.head_node.next_pointer = self.tail_node
		self.tail_node.prev_pointer = self.head_node

	def __contains__(self, key):
		return self.hash.get(key) is not None

	def __len__(self):
		return len(self.hash.keys())

	def get(self, key):
		if self.hash.get(key) is not None:
			return self.hash.get(key).get_value()
		else:
			return -1

	def add_node_to_head(self, key, value):
		# Check if node is already in and raise error if it is
		if key in self:
			raise ValueError("The node you tried to add is already in the hash")

		# New node
		self.hash[key] = self.DoublyLinkedNode(key, value)

		# Set new node's pointers
		self.hash[key].next_pointer = self.head_node.next_pointer
		self.hash[key].prev_pointer = self.head_node

		# Adjust surrounding nodes
		self.head_node.next_pointer.prev_pointer = self.hash[key]
		self.head_node.next_pointer = self.hash[key]

	def update_node_value(self, key, value):
		self.hash[key].set_value(value)

	def remove_tail_node(self):
		if self.tail_node.prev_pointer is self.head_node:
			return
		else:
			# Remove from hash
			last_node_key = self.tail_node.prev_pointer.key
			self.hash.pop(last_node_key)

			# Excise node
			self.tail_node.prev_pointer.prev_pointer.next_pointer = self.tail_node
			self.tail_node.prev_pointer = self.tail_node.prev_pointer.prev_pointer

	def move_node_to_head(self, key):
		current_node = self.hash[key]

		# Excise the node out of the list
		current_node.prev_pointer.next_pointer = current_node.next_pointer
		current_node.next_pointer.prev_pointer = current_node.prev_pointer

		# Add it back in at the head
		current_node.next_pointer = self.head_node.next_pointer
		current_node.prev_pointer = self.head_node

		# Adjust surrounding nodes
		self.head_node.next_pointer.prev_pointer = current_node
		self.head_node.next_pointer = current_node

	def to_string(self):
		node = self.head_node
		output_string = ""
		output_string += node.to_string()
		while node.next_pointer is not None:
			node = node.next_pointer
			output_string += " <-> " + node.to_string()
		return output_string




class LRUCacheConstantTime:
	def __init__(self, capacity):
		"""
		:type capacity: int
		"""
		self.capacity = capacity
		self.cache = DoublyLinkedHashList()

	def get(self, key):
		"""
		:rtype: int
		"""
		if key in self.cache:
			self.cache.move_node_to_head(key)
			return self.cache.get(key)
		else:
			return -1

	def set(self, key, value):
		"""
		:type key: int
		:type value: int
		:rtype: nothing
		"""

		# First check if node is already in
		if key not in self.cache:
			self.cache.add_node_to_head(key, value)
		else:
			self.cache.move_node_to_head(key)
			self.cache.update_node_value(key, value)
		if len(self.cache) > self.capacity:
			self.cache.remove_tail_node()

def test_lru_cache(capacity, commands=None):
	if commands is None:
		return

	cache = LRUCacheConstantTime(capacity)
	correct_cache = LRUCache(capacity)
	for c in commands:
		# Set command
		if len(c) == 2:
			cache.set(c[0], c[1])
			correct_cache.set(c[0], c[1])

		else:
			print "For the key value of {0} correct is {1} and constant time is {2}".format(c[0],
			                                                                                correct_cache.get(c[0]),
			                                                                                cache.get(c[0]))
			assert correct_cache.get(c[0]) == cache.get(c[0])
	print "Finished testing without error."


commands = [[2, 1], [1, 1], [2, 3], [4, 1], [1], [2]]
test_lru_cache(2, commands)

commands = [[2, 1], [2], [3, 2], [2], [3]]
test_lru_cache(1, commands)

commands = [[2, 1], [1, 1], [2], [4, 1], [1], [2]]
test_lru_cache(2, commands)

commands = [[2, 1], [2, 2], [2], [1, 1], [4, 1], [2]]
test_lru_cache((2, commands))

commands = [[2], [2, 6], [1], [1, 5], [1, 2], [1], [2]]
test_lru_cache(2, commands)

commands = [[2, 1], [2], [3, 2], [2], [3]]
test_lru_cache(1, commands)
