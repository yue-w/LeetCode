"""
zipper lists
Write a function, zipper_lists, that takes in the head of two linked lists as arguments. 
The function should zipper the two lists together into single linked list by alternating nodes. 
If one of the linked lists is longer than the other, the resulting list should terminate with 
the remaining nodes. The function should return the head of the zippered linked list.
Do this in-place, by mutating the original Nodes.
You may assume that both input lists are non-empty.
"""

def zipper_lists(head_1, head_2):
  head = head_1
  current = head_1
  current1 = head_1.next
  current2 = head_2
  
  counter = 0
  while current1 and current2:
    if counter % 2 == 0:
      current.next = current2
      current2 = current2.next
    else:
      current.next = current1
      current1 = current1.next
    current = current.next
    counter += 1
    
  if current2:
    current.next = current2 
  if current1:
    current.next = current1

    
  return head