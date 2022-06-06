
from typing import Optional

##Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.method1(l1, l2)
        #return self.method2(l1, l2)
        
    def method1(self, l1, l2):
        """
        Simulate summation directly
        """
        dummy = ListNode()
        curr = dummy
        carry = 0
        
        while l1 or l2 or carry:
            if not l1:
                v1 = 0
            else:
                v1 = l1.val
            if not l2:
                v2 = 0
            else:
                v2 = l2.val
            v = v1 + v2 + carry
            if v >= 10:
                curr.next = ListNode(v - 10)
                carry = 1
            else:
                curr.next = ListNode(v)
                carry = 0
            curr = curr.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
        return dummy.next
        
        
    def method2(self, l1, l2):    
        """
        Cast the list to number and then cast number to list
        """
        v1 = self.list_to_num(l1)
        v2 = self.list_to_num(l2)
        head = self.num_to_list(v1 + v2)
        return head
    
    def list_to_num(self, head):
        """
        List to number
        """
        rst = 0
        tail = head
        power = 0
        while tail:
            rst += tail.val * (10 ** power)
            power += 1
            tail = tail.next
        return rst
            
        
    def num_to_list(self, num):
        """
        Number to list
        """
        if num == 0:
            return ListNode(0)
        dummy = ListNode()
        curr = dummy
        while num:
            curr.next = ListNode(num % 10)
            curr = curr.next
            num = num // 10 
        
        return dummy.next