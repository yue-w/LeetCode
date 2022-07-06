"""
zipper lists
Write a function, zipper_lists, that takes in the head of two linked lists as arguments. 
The function should zipper the two lists together into single linked list by alternating nodes. 
If one of the linked lists is longer than the other, the resulting list should terminate with 
the remaining nodes. The function should return the head of the zippered linked list.
Do this in-place, by mutating the original Nodes.
You may assume that both input lists are non-empty.
"""
## Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def mix_two_linked_list(h1, h2):
  """
  Combine two linked list.
  Example: h1 = [1,2,3,4], h2 = [5,6,7,8]
  h1 = [1,5,2,6,3,7,4,8]
  do NOT return anything, change inplace.
  """
  dummy = ListNode()
  curr = dummy
  while h1 or h2:
      if h1:
          curr.next = h1
          h1 = h1.next
          curr = curr.next
      if h2:
          curr.next = h2
          h2 = h2.next
          curr = curr.next

h1 = ListNode(1)
h1.next = ListNode(2)
h1.next.next = ListNode(3)
h1.next.next.next = ListNode(4)
h2 = ListNode(5)
h2.next = ListNode(6)
h2.next.next = ListNode(7)
# h2.next.next.next = ListNode(8)
# h2.next.next.next.next = ListNode(9)
mix_two_linked_list(h1, h2)
print('Mixed linkedlist:')
while h1:
    print(h1.val)
    h1 = h1.next
