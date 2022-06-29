
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        pre = dummy
        cur = head
        
        while cur:
            ## if find duplite, move pointer to the last one of duplicate,
            ## then set the previous pointer point to the next of duplicate.
            if cur.next and cur.val == cur.next.val:
                ## now we find duplicate, move cur to the last one with the same value
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                ## point pre to cur.next
                pre.next = cur.next
                ## move cur to the next value, which is different
                cur = cur.next
            else:
                pre = pre.next
                cur = cur.next
        
        
        return dummy.next