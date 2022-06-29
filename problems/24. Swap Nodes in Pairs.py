from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next:
            return head
        
        dummy = ListNode()
        dummy.next = head
        pre = dummy
        cur = head
        nxt = head.next
        
        while cur and nxt:
            nxtnxt = nxt.next
            pre.next = nxt
            nxt.next = cur
            cur.next = nxtnxt
            
            if nxtnxt and nxtnxt.next:
                curcp = cur
                cur = nxtnxt
                nxt = nxtnxt.next
                pre = curcp
            else:
                break
        
        
        
        return dummy.next
        
"""
3 nodes?
5 nodes?
"""