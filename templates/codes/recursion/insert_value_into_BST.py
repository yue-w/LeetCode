"""
Insert a value into a binary search tree (BST). keep the property of the BST.
Left tree is maller than or equal to node. Right tree larger than node. 
"""
#%%
class Node:
	def __init__(self, value=None) -> None:
		self.value = value
		self.left = None 
		self.right = None

def insert_into_BST(head, node):
	## if node is None, return head
	if not node.value:
		return head
	## if head is None, return node
	if not head:
		return node
	recursion(head, node)
	return head


def recursion(head, node):
	if node.value <= head.value:
		if head.left:
			recursion(head.left, node)
		else:
			head.left = node
			return 
	else:
		if head.right:
			recursion(head.right, node)
		else:
			head.right = node 
			return 

def print_tree_NLR(head):
	if not head:
		return 
	print(head.value)
	print_tree_NLR(head.left)
	print_tree_NLR(head.right)
#%%		
if __name__ == '__main__':
	node = Node(10)
	node.left = Node(7)
	node.left.left = Node(6)
	node.left.right = Node(9)
	node.right = Node(13)
	node.right.left = Node(11)
	node.right.right = Node(14)
	print("Before:")
	print_tree_NLR(node)
	node_insert = Node(8)
	insert_into_BST(node, node_insert)
	print('After:')
	print_tree_NLR(node)


	

	

# %%
