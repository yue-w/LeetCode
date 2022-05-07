"""
Find the middle node of a linked list
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_mid_node(head):
    ## Use two pointers to find the middle of the linked list.
    ## Even length: fist half and second have the same length
    ## Odd length: first half has one more than the second half.
    ## return the head of the head of the second half.

    slow = head
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow