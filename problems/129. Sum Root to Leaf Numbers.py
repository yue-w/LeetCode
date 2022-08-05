
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, cur):
            ## base case:
            if not node:
                return 0
            cur = 10 * cur + node.val
            
            ## leaf node
            if not node.left and not node.right:
                return cur
            
            return dfs(node.left, cur) + dfs(node.right, cur)
            
            
        return dfs(root, 0)
        