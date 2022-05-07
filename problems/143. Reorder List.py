from typing import Optional
## Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        ## Use two pointers to find the middle of the linked list.
        ## Even length: fist half and second have the same length
        ## Odd length: first half has one more than the second half.
        dummy = ListNode()
        dummy.next = head
        slow = head 
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        ## the linked list has been breaked to two from the middle
        h1 = head
        h2 = slow.next
        ## Break the link between the first and the second linked list
        slow.next = None

        ## call helper function to reverse the second half of linked list
        h2 = self._reverse_linked_list(h2)
        h = dummy
        while h1 or h2:
            if h1:
                h.next = h1
                h1 = h1.next 
                h = h.next
            if h2:
                h.next = h2  
                h2 = h2.next
                h = h.next

    def _reverse_linked_list(self, head):
        prev = None
        cur = head
        nxt = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return prev






if __name__ == '__main__':
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)
    node.next.next.next.next = ListNode(5)
    s = Solution()
    s.reorderList(node)

    while node:
        print(node.val)
        node = node.next
