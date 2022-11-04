from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next:
            return head

        ## length is the number of nodes in the linkedlist
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        
        kk = k % length
        if kk == 0:
            return head
        
        dummy = ListNode()
        dummy.next = head
        
        cur = dummy
        step = 0
        while step < length - kk:
            step += 1
            cur = cur.next
        nxt = cur.next
        cur.next = None
        
        dummy.next = nxt
        
        while nxt.next:
            nxt = nxt.next
        
        nxt.next = head
        
        return dummy.next
        
        