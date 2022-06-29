

#### Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge sort with iteration
        """
        ## Corner cases: if 0 or 1 element, return 
        if not head:
            return head
        if not head.next:
            return head
        

        dummy = ListNode()
        dummy.next = head
        curr = head 
        ## get the length of the LinkedList
        length = 0
        while curr:
            length += 1
            curr = curr.next
        
        n = 1
        while n < length:
            pre = dummy
            cur =  dummy.next
            while cur:
                left = cur
                right = self.split(left, n)
                cur = self.split(right, n)
                small, large = self.merge(left, right)
                pre.next = small
                pre = large
            n *= 2
            
        return dummy.next
            
    def split(self, head, n):
        """
        Split the list to two parts. 
        First part starts from head and has n elements
        Return head of the second part
        """
        while n - 1 and head:
            head = head.next
            n -= 1
        if head:   
            nxt = head.next
            head.next = None
        else:
            nxt = None
        return  nxt
        
    def merge(self, left, right):
        """
        Merge two LinkedList, left and right. Ascending order.
        Return the first and last node of the LinkedList.
        """
        dummy = ListNode()
        cur = dummy
        while left and right:
            if left.val < right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        if left:
            cur.next = left
        if right:
            cur.next = right
        
        while cur.next:
            cur = cur.next
        
        return dummy.next, cur
        
if __name__ == '__main__':
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)
    rst = Solution().sortList(head)
    while rst:
        print(rst.val)
        rst = rst.next