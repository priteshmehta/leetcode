#Tree traversal in python

class Node:
    """
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert_node(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert_node(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert_node(data)      
        else:
            self.data = data

    def find_node(self, data):
        if data < self.data:
            if self.left is None:
                return "{} Not found".format(data)
            else:
                return self.left.find_node(data)
        elif data > self.data:
            if self.right is None:
                return "{} Not found".format(data)
            else:
                return self.right.find_node(data)   
        else:
            return "{} Found".format(data)
        
    def preorder_traverse(self):
        if self.left:
            self.left.preorder_traverse()
        print(self.data)
        if self.right:
            self.right.preorder_traverse()

    def inorder_traverse(self):
        print(self.data)
        if self.left:
            self.left.preorder_traverse()
        if self.right:
            self.right.preorder_traverse()

    def postorder_traverse(self):
        if self.left:
            self.left.preorder_traverse()
        if self.right:
            self.right.preorder_traverse()
        print(self.data)
  
root = Node(12) 
root.insert_node(6)
root.insert_node(14)
root.insert_node(3)



print("######### Preorder Traversal #########")
root.preorder_traverse()

print("######### Inoder Traversal #########")
root.inorder_traverse()

print("######### Postorder Traversal #########")
root.postorder_traverse()

print(root.find_node(3))
print(root.find_node(122))