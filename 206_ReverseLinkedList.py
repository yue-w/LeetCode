# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 15:09:01 2020

@author: wyue
"""

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

## Solution 1. Iteration. Runtime: O(n), space O(1)
def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    ## if there is no element or only one element, just return the head
    if head == None or head.next == None: return head
    
    prev = head
    current = prev.next
    
    ## The first node would be the last when reversed.
    prev.next = None
    
    while current.next != None:
        nxt = current.next
        current.next = prev 
        prev = current
        current = nxt
        
    current.next = prev
    
    return current

def helper(head):
    ## Base case:
    if head == None or head.next == None:
        return head
    
    head_rev = helper(head.next)
    head.next.next = head
    head.next = None
    return head_rev
    
    
## Solution 2. Recursion. Runtime: O(n), space O(n)
def reverseList_recursion(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    head = helper(head)
    return head
    



lst = ListNode(0)
lst.next = ListNode(1)
lst.next.next = ListNode(2)
lst.next.next.next = ListNode(3)

head = reverseList_recursion(lst)