
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
            # Base case
            if not head:
                return None
            dummy = ListNode()
            dummy.next = head
            slow = head
            fast = head
            pre = dummy
            while fast and fast.next:
                fast = fast.next.next
                pre = slow
                slow = slow.next
            # Break the linkedlist
            pre.next = None
            root = TreeNode(slow.val)
            root.left = dfs(dummy.next)
            root.right = dfs(slow.next)
            return root

        return dfs(head)