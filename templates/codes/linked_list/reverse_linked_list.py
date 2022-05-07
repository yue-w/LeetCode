
from typing import Optional

from sklearn.linear_model import PassiveAggressiveRegressor
## Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list_iteration(self, head: Optional[ListNode]) -> Optional[ListNode]:
    """
    return the head of the reversed linked list
    """
    prev = None
    cur = head
    nxt = None
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt

    return prev