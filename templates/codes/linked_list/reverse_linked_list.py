#%%
from typing import Optional
from sklearn.linear_model import PassiveAggressiveRegressor

#%%
## Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list_iteration(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    return the head of the reversed linked list
    """
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt

    return prev

#%%
head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head = reverse_linked_list_iteration(head)
while head:
    print(head.val)
    head = head.next
# %%
