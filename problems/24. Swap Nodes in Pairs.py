from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        pre = dummy
        
        while pre.next and pre.next.next:
            curr = pre.next
            nxt = curr.next
            # pre -> curr -> nxt -> nxt.next is changed to pre -> nxt -> curr -> nxt.next 
            pre.next, nxt.next, curr.next = nxt, curr, nxt.next
            pre = curr
        
        return dummy.next