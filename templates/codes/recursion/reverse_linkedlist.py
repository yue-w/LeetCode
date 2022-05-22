
class Node:
	def __init__(self, v):
		self.v = v 
		self.next = None 

class LinkedList:
	def __init__(self, head=None) -> None:
		self.head = head

	def reverse(self, node):
		## Base case
		if (node is None) or (node.next is None):
			return node
		else:
			n = self.reverse(node.next)
			node.next.next = node
			node.next = None ## Don't forget this line.
			return n



	def __str__(self):
		rst = ''
		node = self.head
		while node:
			rst += str(node.v) + ', '
			node = node.next
		return "Values in the linked list: " + rst

if __name__ == '__main__':
	node = Node(0)
	node.next = Node(1)
	node.next.next = Node(2)
	node.next.next.next = Node(3)
	link_list = LinkedList(node)
	print(link_list)
	new_head = link_list.reverse(node)
	rev_link_list = LinkedList(new_head)
	print(rev_link_list)
	print('done')

