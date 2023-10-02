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
        #### Preferred method is method 1
        """
        :type head: Node
        :rtype: Node
        """
        # ## Method One, iterative, use Hash. Preferred method.
        # dic = {}
        # current = head
        
        # ## Iterate all nodes, make a deep copy of all the node, 
        # ## set value of val, ignore next and radnom for now
        # while current:
        #     dic[current] = Node(current.val, None, None)
        #     current = current.next
        
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
        
"""
Method 3, 1 pass
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        created = {}
        dummy = Node(0)
        dummy.next = head
        dummy_cp = Node(0)
        curr = dummy
        curr_cp = dummy_cp
        while curr:
            nxt = curr.next
            if id(nxt) in created:
                curr_cp.next = created[id(nxt)]
            else:
                if nxt:
                    nxt_cp = Node(nxt.val)
                    curr_cp.next = nxt_cp
                    created[id(nxt)] = nxt_cp
                
            random = curr.random
            if id(random) in created:
                curr_cp.random = created[id(random)]
            else:
                if random:
                    curr_cp.random = Node(random.val)
                    created[id(random)] = curr_cp.random
            curr = curr.next
            curr_cp = curr_cp.next

        return dummy_cp.next
"""


head = Node(7,None,None)
head.next = Node(13,None,0)
head.next.next = Node(11,None,4)
head.next.next.next = Node(10,None,2)
head.next.next.next.next = Node(1,None,0)

head = Solution().copyRandomList(head)