# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 15:09:01 2020

@author: wyue
"""
from typing import Optional
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverseList_iteration(head)
    def reverseList_iteration(self, head):
        if not head:
            return head
        cur = head
        prev = None
        tail = None
        while cur:
            tail = cur.next
            cur.next = prev 
            prev = cur
            cur = tail
        return prev
    
    ## Solution 2. Recursion. Runtime: O(n), space O(n)
    def reverseList_recursion(self, head):
        pass
    



lst = ListNode(0)
lst.next = ListNode(1)
lst.next.next = ListNode(2)
lst.next.next.next = ListNode(3)

head = reverseList_recursion(lst)