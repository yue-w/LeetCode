# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 21:07:14 2020

@author: wyue
"""

##Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        slow = dummy
        fast = head
        while n > 0 and fast:
            fast = fast.next
            n -= 1
        while fast:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        
        return dummy.next
        
    
