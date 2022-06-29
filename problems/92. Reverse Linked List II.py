
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        return self.method1(head, left, right)
    
    def method1(self, head, left, right):
        """
        Preferred method
        Time: O(n)
        Space: O(1)
        multiple passes
        """
        dummy = ListNode()
        dummy.next = head
        
        ## truncate the original LinkedList into three parts:
        ## with their head bing first, second, and third
        
        ## get the head of the third part
        cur = dummy
        for _ in range(right):
            cur = cur.next
        third = cur.next
        ## break the second from the third
        cur.next = None
        
        ## get the head of the second part
        cur = dummy
        for _ in range(left-1):
            cur = cur.next
        second = cur.next
        ## break the first from the second
        cur.next = None
        
        ## reverse the second part using a "sliding window"
        second = self.reverse(second)
        
        ## the head of the first part is head
        first = dummy
        ## point the head of first to the tail of the second
        while first.next:
            first = first.next
        first.next = second
        
        ## point the head of second to the tail of the tail of the third
        while second.next:
            second = second.next
        second.next = third        
        
        return dummy.next
    
    def reverse(self, head):
        """
        Reverse a LinkedList using "Sliding window"
        """
        pre = None
        cur = head
        
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        
        return pre
        
    def method2(self, head, left, right):
        """
        One pass.
        """
        pass

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next= ListNode(4)
    head.next.next.next.next = ListNode(5)
    left = 2
    right = 4
    rst = Solution().reverseBetween(head, left, right)

    while rst:
        print(rst.val)
        rst = rst.next
