"""
rite a function, tree_sum, that takes in the root of a binary tree that 
contains number values. The function should return the total sum of all 
values in the tree.
"""
from queue import Queue

class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def tree_sum(root, method='recursion'):
	if method == 'recursion':
		if not root:
			return 0
		return root.val + tree_sum(root.left) + tree_sum(root.right)
	elif method =='iteration_dfs':
		return iteration_dfs(root)
	elif method == 'iteration_bfs':
		return iteration_bfs(root) 
	
def recursion(root):
	if not root:
		return 0
	return root.val + recursion(root.left) + recursion(root.right)

def iteration_dfs(root):
	rst = 0
	if not root:
		return rst
	stack = [root]
	while stack:
		node = stack.pop()
		rst += node.val
		if node.left:
			stack.append(node.left)
		if node.right:
			stack.append(node.right)

	return rst

def iteration_bfs(root):
	rst = 0
	if not root:
		return rst 
	q = Queue()
	q.put(root)
	while not q.empty():
		node = q.get()
		rst += node.val
		if node.left:
			q.put(node.left)
		if node.right:
			q.put(node.right)
	return rst


	
if __name__ == '__main__':
	a = Node(3)
	b = Node(11)
	c = Node(4)
	d = Node(4)
	e = Node(-2)
	f = Node(1)

	a.left = b
	a.right = c
	b.left = d
	b.right = e
	c.right = f

	#       3
	#    /    \
	#   11     4
	#  / \      \
	# 4   -2     1

	assert tree_sum(a, method='iteration_bfs') == 21
	a = Node(1)
	b = Node(6)
	c = Node(0)
	d = Node(3)
	e = Node(-6)
	f = Node(2)
	g = Node(2)
	h = Node(2)

	a.left = b
	a.right = c
	b.left = d
	b.right = e
	c.right = f
	e.left = g
	f.right = h

	#      1
	#    /   \
	#   6     0
	#  / \     \
	# 3   -6    2
	#    /       \
	#   2         2

	assert tree_sum(a, method='iteration_bfs') == 10
	assert tree_sum(None) == 0

	print("All test passed")