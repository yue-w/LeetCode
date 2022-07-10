
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.rst = 0
        self.dfs(root, 0)
        return self.rst
    
    def dfs(self, node, v):
        ## base case
        if not node:
            return 

        v = 10 * v + node.val
        ## if leaf node, add val to self.rst
        if not node.left and not node.right:
            self.rst += v
        self.dfs(node.left, v)
        self.dfs(node.right, v)
        