
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #return self.method1(head)
        return self.method2(head) 
        
        
    def method1(self, head):
        """
        Time: O(n)
        Space: O(n)
        """
        nums = []
        curr = head
        while curr:
            nums.append(curr.val)
            curr = curr.next
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] != nums[j]:
                return False
            i += 1
            j -= 1
        return True
    
    def method2(self, head):
        """
        Time: O(n)
        Space: O(1)
        """
        ## reverse second half of the linked list. ## restore the linkedlist before returning it
        
        def reverse_linkedlist(head):
            """
            Reverse a linked with "head" as head. Return the new head
            """
            pre = None
            curr = head
            while curr:
                nxt = curr.next
                curr.next = pre
                pre = curr
                curr = nxt
            return pre
        
        ## use two runners to find the mid node
        ## at the end, slow.next is head2
        dummy = ListNode()
        dummy.next = head
        slow = dummy
        fast = dummy
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        head2 = slow.next
        h1 = dummy.next
        h2 = head2
        h2 = reverse_linkedlist(h2)
        while h1 and h2:
            if h1.val != h2.val:
                return False
            h1 = h1.next
            h2 = h2.next
        
        
        tail1 = slow
        head2 = reverse_linkedlist(h2)
        tail1.next = head2
        return True