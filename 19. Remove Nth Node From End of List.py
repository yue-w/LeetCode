# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 21:07:14 2020

@author: wyue
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next is None:
            return None
        
        ## To do check n == 2
        
        runner = head
        current = head
        for i in range(n):
            if not runner.next:
                return current.next
            runner = runner.next
        while runner.next:
            runner = runner.next
            current = current.next
        current.next = current.next.next
        return head
        
    
