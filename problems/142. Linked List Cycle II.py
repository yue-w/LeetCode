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
 
"""
Let C be the steps the slow pointer has gone when the two pointers meet, then the fast
pointer gas gone 2C steps when they meet.
Let L be the steps between the starting point and the cycle (short for "the node where the cycle begins"). 
Let M be the steps the slow pointer has gone after it reached the cycle.
Then the slow pointer has gone the following steps:
SLOW = L + M,  -------- (1)
and the fast pointer has gone the following steps:
FAST = 2 * SLOW = L + K * circle + M,  ----------(2)
where, K is a constant (how many circles the fast pointer has gone after it reached the cycle),
and circle is the circumference of the cycle.
Solving equations (1) and (2) we have
L + M = K * circle, 
which means if we let a new pointer starts from the head, and another new pointer starts from
the point where the fast and slow pointer first met, and the two new pointers moves at the same speed,
when the two new pointers meet, they will be at the cycle ("the node where the cycle begins").
"""