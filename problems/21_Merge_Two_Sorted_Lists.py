# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 22:20:03 2020

@author: wyue
"""
from typing import Optional

##Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ## Method 1: iteration
        #return self.iteration(list1, list2)
        ## Method 2: reucrsion
        dummy = ListNode()
        tail = dummy 
        self.recursion(tail, list1, list2)
        return dummy.next
        
    def iteration(self, list1, list2):
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        else:
            tail.next = list2
            
        return dummy.next

    def recursion(self, tail, list1, list2):
        ## Base case:
        if not list1:
            tail.next = list2
            return 
        elif not list2:
            tail.next = list1
            return 
        if list1.val < list2.val:
            tail.next = list1 
            tail = tail.next
            self.recursion(tail, list1.next, list2)
        else:
            tail.next = list2 
            tail = tail.next
            self.recursion(tail, list1, list2.next)


if __name__ == '__main__':
    l1 = ListNode(-9)
    l12 = ListNode(3)
    #l13 = ListNode(4)
    l1.next = l12
    #l12.next = l13

    l2 = ListNode(5)
    l22 = ListNode(7)
    #l23 = ListNode(4)

    l2.next = l22
    #l22.next = l23
    s = Solution()
    lout = s.mergeTwoLists(l1,l2)
    while lout!=None:
        print(lout.val)
        lout = lout.next



        