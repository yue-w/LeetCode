from queue import Queue
class Node:
	def __init__(self, value=None, left=None, right=None) -> None:
		self.value = value 
		self.left = left 
		self.right = right

def bfs(root):
	if not root:
		return [root]
	rst = []
	queue = Queue()
	queue.put(root)
	while not queue.empty():
		node = queue.get()
		rst.append(node.value)
		if node.left:
			queue.put(node.left)
		if node.right:
			queue.put(node.right)
	return rst

if __name__ == '__main__':
	root = Node('a')
	root.left = Node('b')
	root.left.left = Node('d')
	root.left.right = Node('e')
	root.right = Node('c')
	root.right.right = Node('f')

	nodes = bfs(root)
	print(nodes)
