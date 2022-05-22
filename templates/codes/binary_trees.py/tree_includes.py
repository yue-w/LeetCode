"""
tree includes
Write a function, treeIncludes, that takes in the root of a binary tree and a 
target value. The function should return a boolean indicating whether or not 
the value is contained in the tree.
"""
from operator import rshift
from queue import Queue

class Node:
	def __init__(self, value=None, left=None, right=None) -> None:
		self.value = value 
		self.left = left 
		self.right = right

def tree_includes_bfs(root, value):
	if not root:
		return False
	queue = Queue()
	queue.put(root)
	while not queue.empty():
		node = queue.get()
		if node.value == value:
			return True 
		else:
			if node.left:
				queue.put(node.left)
			if node.right:
				queue.put(node.right)

	return False


def tree_includes_dfs(root, value):
	if not root:
		return False 
	if root.value == value:
		return True
	
	if root.left:
		left = tree_includes_dfs(root.left, value)
	else:
		left = False
	if root.right:
		right = tree_includes_dfs(root.right, value)
	else:
		right = False 
	if left or right:
		return True 
	else:
		return False

if __name__ == '__main__':
	root = Node('a')
	root.left = Node('b')
	root.left.left = Node('d')
	root.left.right = Node('e')
	root.right = Node('c')
	root.right.right = Node('f')

	rst = tree_includes_bfs(root, 'e')
	print(rst)