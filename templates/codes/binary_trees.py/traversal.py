class Node:
	def __init__(self, value=None, left=None, right=None) -> None:
		self.value = value 
		self.left = left 
		self.right = right
def level_order_traversal(root):
	pass
def dfs_iteration_preorder_NLR(root):
	rst = []
	if not root:
		return rst 

	stack = []
	stack.append(root)

	while stack:
		node = stack.pop()
		rst.append(node.value)
		if node.right:
			stack.append(node.right)
		if node.left:
			stack.append(node.left)

	return rst

def dfs_recursion_preorder_NLR(root, rst=None):
	## base case
	if not root:
		return 
	rst.append(root.value)
	dfs_recursion_preorder_NLR(root.left, rst)
	dfs_recursion_preorder_NLR(root.right, rst)

def dfs_iteration_inorder_LNR(root):
	rst = []
	stack = []
	pointer = root 
	while stack or pointer:
		while pointer:
			stack.append(pointer)
			pointer = pointer.left
		pointer = stack.pop()
		rst.append(pointer.value)
		pointer = pointer.right

	return rst
	
def dfs_recursion_inorder_LNR(root, rst):
	## base case
	if not root:
		return
	dfs_recursion_inorder_LNR(root.left, rst)
	rst.append(root.value)
	dfs_recursion_inorder_LNR(root.right, rst)

def dfs_recursion_postorder_LRN():
	pass 

def def_iteration_postorder_LRN():
	pass


if __name__ == '__main__':
	"""
				a
			  /   \
			b       c
		  /   \    / 
		d      e  f	   
	"""
	root = Node('a')
	root.left = Node('b')
	root.left.left = Node('d')
	root.left.right = Node('e')
	root.right = Node('c')
	root.right.left = Node('f')
	#root.right.right = Node('g')

	nodes = dfs_iteration_preorder_NLR(root)
	print(nodes) # a b d e c f
	nodes = []
	dfs_recursion_preorder_NLR(root, nodes)
	print(nodes)
	nodes = []
	dfs_recursion_inorder_LNR(root, nodes)
	print(nodes)
	nodes = dfs_iteration_inorder_LNR(root)
	print(nodes)

