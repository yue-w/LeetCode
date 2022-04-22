# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 09:45:18 2020

@author: wyue
"""
import heapq
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        ListNode.__lt__ = lambda x, y: True if x.val < y.val else False # key statement
        
        if not lists:
            return []
        
        dummy = ListNode(None)
        curr = dummy
        heap = [(node.val, node) for node in lists if node]
        
        heapq.heapify(heap)
        while heap:
            val, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, node.next))
            
        return dummy.next
        

        


lists = []

l = ListNode(1)
l.next = ListNode(4)
l.next.next = ListNode(5)
lists.append(l)

l = ListNode(1)
l.next = ListNode(3)
l.next.next = ListNode(4)
lists.append(l)

l = ListNode(2)
l.next = ListNode(6)
lists.append(l)
l = Solution().mergeKLists(lists)