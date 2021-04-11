
#Implementing Hash table using array with collision resolution

class HashNode:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.next = None

class HashTable:
	def __init__(self, initial_value=50):
		self.capacity = initial_value
		self.bucket = []
		self.size = 0

	def hash_function(self, key):
		#assumiing key is string
		#hash value = index + length of key + ascii value of each char
		hash_sum = 0
		for idx, c in enumerate(key):
			hash_sum += (idx + len(key)) ** ord(c)
		hash_sum = hash_sum % self.capacity
		print hash_sum
		return hash_sum

	def add(self, key, value):
		self.size += 1
		index = self.hash_function(key)
		try:
			self.bucket[index]
			#TBD  - collision resolution
		except KeyError:
			self.bucket[index] = HashNode(key, value)

	def get(self, key):
		index = self.hash_function(key)
		node = self.bucket[index]
		while node != None:
			if node.key == key:
				return node.value
			node = node.next
		return -1

	def size(self):
		return self.size



h = HashTable(100)
h.hash_function("appla")
h.hash_function("apple")
h.hash_function("orange")
h.hash_function("abc")
h.hash_function("a")
h.hash_function("p")