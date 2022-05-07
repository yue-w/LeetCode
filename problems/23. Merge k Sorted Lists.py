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
        Method 1: Use heap
        Time: O(nklogk)
        Space: O(k)
        """
        ListNode.__lt__ = lambda x, y: True if x.val < y.val else False # key statement

        rst = ListNode()
        head = rst
        heap = [node for node in lists if node]
        heapq.heapify(heap)
        
        while heap:
            node = heapq.heappop(heap)
            head.next = node
            if node.next:
                heapq.heappush(heap, node.next)
            head = head.next
            
        
        return rst.next

        """
        Method 2: divde and conquer
        Time: O(nklogk)
        Space: O(logk) if recursion or O(1) if iteration.
        """
        ## Todo



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
#l = Solution().mergeKLists([])
while l:
    print(l.val)
    l = l.next