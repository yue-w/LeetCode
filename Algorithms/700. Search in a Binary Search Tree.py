
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        
        def dfs(node, val):
            ## base case. None
            if not node:
                return None
            if val == node.val:
                return node
            if val < node.val:
                return dfs(node.left, val)
            else:
                return dfs(node.right, val)
            
        return dfs(root, val)