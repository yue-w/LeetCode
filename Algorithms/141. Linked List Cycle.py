from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        """
        Solution of O(1) space
        """
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True

        return False
        
        # """
        # Solution of O(n) space
        # """
        # seen = set()
        # dummy = ListNode(-1, head)
        # while head:
        #     if id(head) in seen:
        #         return True
        #     seen.add(id(head))
        #     head = head.next
        # return False