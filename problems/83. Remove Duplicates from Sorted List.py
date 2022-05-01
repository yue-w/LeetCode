# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 18:00:07 2020

@author: wyue
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        dummy = head
        while(head):
            nxt = head.next       
            while nxt:
                if head.val == nxt.val:
                    nxt = nxt.next
                else:
                    head.next = nxt
                    break
            head = nxt
            
        return dummy 