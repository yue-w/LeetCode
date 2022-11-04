
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def dfs(head):
            """
            truncate the linkedlist in the middle. The left part belongs to the left tree,
            the right part belongs to the right tree. The mid point is the root. 
            """
            ## base case
            if not head:
                return None
            
            ## find the mid point of the linkedlist
            dummy = ListNode()
            dummy.next = head
            fast = head
            slow = dummy
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            
            mid = slow.next
            ## cut the fist and second half
            slow.next = None
            
            node = TreeNode(mid.val)
            
            node.left = dfs(dummy.next)
            node.right = dfs(mid.next)
            
            return node
        
        ## if no node
        if not head:
            return
        ## if only one node
        if not head.next:
            return TreeNode(head.val)
        return dfs(head)