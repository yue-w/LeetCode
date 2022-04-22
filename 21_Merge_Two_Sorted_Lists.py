# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 22:20:03 2020

@author: wyue
"""

class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
         


def mergeTwoLists(l1,l2):
    dummy = ListNode(-1)
    head = dummy
    
    while l1!=None and l2!=None:
        if l1.val<=l2.val:
            dummy.next = l1
            l1 = l1.next
        else:
            dummy.next = l2
            l2 = l2.next
        dummy = dummy.next
    if l1 != None:
        dummy.next = l1
    else:
        dummy.next = l2
    
    return head.next


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

lout = mergeTwoLists(l1,l2)
while lout!=None:
    print(lout.val)
    lout = lout.next



        