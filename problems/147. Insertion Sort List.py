
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head
        
        cur = head
        pre = dummy
        while cur:
            while cur.next and cur.val <= cur.next.val:
                pre = cur
                cur = cur.next
            
            ## when reaching this point, two cases:
            
            ## case 1:
            ## if cur is the last node
            if cur and not cur.next:
                return dummy.next
            
            ## case 2: cur.next is not None, and cur.val > cur.next.val
            to_insert = cur.next
            # pre = cur
            # cur = to_insert.next
            # pre.next = cur
            cur.next = to_insert.next
            self.insert(dummy, to_insert)
            
        return dummy.next
    
    def insert(self, dummy, to_insert):
        """
        insert ListNode "to_insert" to the LinkedList with head "head"
        when calling this function, to_insert.val must be smaller than the value of the last node
        in the linkedlist
        """
        pre = dummy
        cur = pre.next
        
        while cur and to_insert.val > cur.val:
            pre = cur
            cur = cur.next
        pre.next = to_insert
        to_insert.next = cur
        
            
            
