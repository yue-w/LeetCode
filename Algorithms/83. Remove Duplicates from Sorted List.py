# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 18:00:07 2020

@author: wyue
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        
        curr = head
        
        while curr:
            while curr.next and curr.val == curr.next.val:
                curr.next = curr.next.next
            curr = curr.next
        
        return dummy.next