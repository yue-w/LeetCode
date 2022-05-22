class Node:
	def __init__(self, v=None):
		self.v = v 
		self.next = None 

class LinkedList:
	def __init__(self, head=None) -> None:
		self.head = head

	def __str__(self):
		rst = ''
		node = self.head
		while node:
			rst += str(node.v) + ', '
			node = node.next
		return "Values in the linked list: " + rst

def merge_two_sorted_linked_list(sll1, sll2):
	dummy = Node()
	recursion(dummy, sll1.head, sll2.head)
	return LinkedList(dummy.next)
	 

def recursion(node, node1, node2):
	## Base case
	if node1 is None:
		node.next = node2
		return 
	if node2 is None:
		node.next = node1
		return 
	## recursion
	if node1.v < node2.v:
		node.next = node1
		node1 = node1.next
	else:
		node.next = node2
		node2 = node2.next
	recursion(node.next, node1, node2)

if __name__ == '__main__':
	node = Node(-1)
	node.next = Node(1)
	node.next.next = Node(3)
	node.next.next.next = Node(5)
	node.next.next.next.next = None
	link_list1 = LinkedList(node)
	print(link_list1)
	node = Node(0)
	node.next = Node(2)
	node.next.next = Node(4)
	node.next.next.next = Node(6)
	node.next.next.next.next = None
	link_list2 = LinkedList(node)
	print(link_list2)

	merged_list = merge_two_sorted_linked_list(link_list1, link_list2)
	print(merged_list)