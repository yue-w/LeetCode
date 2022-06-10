from typing import Optional

## Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Edge cases, 0, 1, and 2 nodes
        """
        if (not head) or (not head.next) or (not head.next.next):
            return head

        dummy_odd = ListNode()
        dummy_odd.next = head
        odd_curr = head
        
        
        dummy_even = ListNode()
        dummy_even.next = head.next
        even_curr = head.next
        
        
        while odd_curr.next and odd_curr.next.next:
            odd_curr.next = odd_curr.next.next
            odd_curr = odd_curr.next   

            even_curr.next = even_curr.next.next
            even_curr = even_curr.next
              
        odd_curr.next = dummy_even.next
        
        return dummy_odd.next

if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    #head.next.next.next.next.next = ListNode(5)
    rst = s.oddEvenList(head)
    print(rst)
    while rst:
        print(rst.val)
        rst = rst.next