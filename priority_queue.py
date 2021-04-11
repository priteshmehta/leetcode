#implementing priority queue

class PriorityQueue:
	def __init__(self):
		self.queue = []

	def enqueu(self, data):
		self.queue.append(data)

	def __str__(self):
		return str(self.queue)

	#deque based on the value
	def dequeue(self):
		if len(self.queue) == 0:
			return -1

		i = max_index = 0
		while i < len(self.queue):
			if self.queue[i] > self.queue[max_index]:
				max_index = i

			i += 1
		data = self.queue[max_index]
		del self.queue[max_index]
		return data


pr = PriorityQueue()
pr.enqueu(11)
pr.enqueu(1)
pr.enqueu(12)
pr.enqueu(14)
pr.enqueu(5)

print(pr)

print("dequeue: ", pr.dequeue())
print("dequeue: ", pr.dequeue())
print("dequeue: ", pr.dequeue())


print(pr)