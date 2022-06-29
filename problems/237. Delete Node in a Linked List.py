# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 18:10:24 2020

@author: wyue
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        nextNode = node.next
        node.val = nextNode.val
        node.next = nextNode.next  

if __name__ == '__main__':
    node = ListNode(4)
    node.next = ListNode(5)
    node.next.next = ListNode(1)
    node.next.next.next = ListNode(9)
    Solution().deleteNode(node.next)
    while node:
        print(node.val)
        node = node.next