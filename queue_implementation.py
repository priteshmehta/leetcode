#queue implementation
import sys

MAXSIZE = sys.maxint
class Queue:
	# pointer , front/head , and rear/tail
	def __init__(self):
		self.head = None
		self.__queue_data = []
		self.capacity = MAXSIZE

	def enqueue(self, data):
		self.__queue_data.append(data)
		if len(self.__queue_data) == 1:
			self.head = 0

	def dequeue(self):
		if self.head != None:
			value = self.__queue_data[self.head]
			self.head += 1
			return value
		else:
			print("nothing to return")
			return

	def peek(self):
		# returns the peek element without removing it
		return self.__queue_data[self.head]

	def get_all(self):
		return self.__queue_data[self.head:]

	def size(self):
		return len(self.__queue_data[self.head:])


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print("Queue:", q.get_all())
q.dequeue()
q.dequeue()
print(q.get_all())
