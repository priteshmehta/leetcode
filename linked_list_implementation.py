#Linked list implementation
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class DNode:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

class SingleLinkedList:
	def __init__(self):
		self.head = None


	def append_node(self, data):
		node = Node(data)
		if self.head == None:
			self.head = node
		else:
			last_node = self.get_last_node()
			last_node.next = node

	def get_last_node(self):
		node = self.head
		while(node.next != None):
			node = node.next
		return node

	def show(self):
		node = self.head
		while(node != None):
			print(node.data)
			node = node.next

	def reverse(self):
		node = self.head
		prev_node = None
		while(node != None):
			next_node = node.next
			node.next = prev_node
			prev_node = node
			node = next_node

		self.head = prev_node

	def get_head(self):
		return self.head


def test_singleLinkedList():
	linked_list = SingleLinkedList()
	linked_list.append_node(10)
	linked_list.append_node(20)
	linked_list.append_node(30)
	linked_list.show()
	print("--- Reverse ----")
	linked_list.reverse()
	linked_list.show()

def merge_sorted_linked_list():
	linked_list1 = SingleLinkedList()
	linked_list1.append_node(10)
	linked_list1.append_node(20)
	linked_list1.append_node(30)

	linked_list2 = SingleLinkedList()
	linked_list2.append_node(1)
	linked_list2.append_node(25)
	linked_list2.append_node(30)
	linked_list2.append_node(50)
	linked_list2.append_node(51)

	# Merge two sorted singly Linked lists
	linked_list3 = SingleLinkedList()
	node1 = linked_list1.get_head()
	node2 = linked_list2.get_head()

	while node1 != None and node2 != None:
		if node1.data < node2.data:
			linked_list3.append_node(node1.data)
			node1 = node1.next
		elif node2.data < node1.data:
			linked_list3.append_node(node2.data)
			node2 = node2.next
		else:
			# append both nodes data if both are equal
			linked_list3.append_node(node1.data)
			linked_list3.append_node(node2.data)
			node1 = node1.next
			node2 = node2.next

	#appending pending elements
	while node1 != None:
		linked_list3.append_node(node1.data)
		node1 = node1.next

	while node2 != None:
		linked_list3.append_node(node2.data)
		node2 = node2.next

	linked_list3.show()

if __name__ == '__main__':
	#test_singleLinkedList()
	merge_sorted_linked_list()

