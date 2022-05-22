class Node:
	def __init__(self, value=None) -> None:
		self.value = value
		self.left = None 
		self.right = None
	
	def print_all_leaf_nodes(self):
		if self.value is None:
			return
		if self.left is None and self.right is None:
			print(self.value)
		if self.left:
			self.left.print_all_leaf_nodes()
		if self.right:
			self.right.print_all_leaf_nodes()
		return

if __name__ == '__main__':
	node = Node(10)
	node.left = Node(7)
	node.left.left = Node(6)
	node.left.right = Node(9)
	node.right = Node(13)
	node.right.left = Node(11)
	node.right.right = Node(14)
	node.print_all_leaf_nodes()