# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 15:26:45 2020

@author: wyue
"""


# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # ## Method One, iterative, use Hash.
        # dic = {}
        # current = head
        
        # ## Iterate all nodes, make a deep copy of all the node, 
        # ## set value of val, ignore next and radnom for now
        # while current:
        #     if not current in dic:
        #         dic[current] = Node(current.val, None, None)
        #         current = current.next
        
        # ## Iterate all nodes, set value of next and random
        # current = head
        # while current:
        #     dic[current].next = dic.get(current.next)
        #     dic[current].random = dic.get(current.random)
        #     current = current.next
            
        # if head in dic:
        #     return dic[head]
        # else:
        #     return None
        
        ## Method 2, recursion
        if not head:
            return None
        if head in self.dic:
            return self.dic.get(head)
        else:
            node = Node(head.val, None, None)
            self.dic[head] = node
            node.next = self.copyRandomList(head.next)
            node.random = self.copyRandomList(head.random)
            
            return node
        
    def __init__(self):
        self.dic = {}
        



head = Node(7,None,None)
head.next = Node(13,None,0)
head.next.next = Node(11,None,4)
head.next.next.next = Node(10,None,2)
head.next.next.next.next = Node(1,None,0)

head = Solution().copyRandomList(head)