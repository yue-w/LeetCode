from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        cycle = False
        
        fast = head
        slow = head
        
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                cycle = True
                break
        
        if not cycle:
            return None
        else:
            while slow:
                if slow == head:
                    return head
                slow = slow.next
                head = head.next
                
            