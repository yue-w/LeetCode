
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_v = float('-inf')
        self.dfs(root)
        return self.max_v 
    
    def dfs(self, node):
        ## Base case
        if not node:
            return 0
        left = self.dfs(node.left)
        left = max(left, 0)
        right = self.dfs(node.right)
        right = max(right, 0)
        to_return = max(left, right) + node.val
        self.max_v = max(self.max_v, left + right + node.val)
        return to_return