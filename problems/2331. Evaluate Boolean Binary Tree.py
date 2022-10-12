from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        
        return self.dfs(root)
        
    def dfs(self, node):
        ## base case: leaf node
        if not node.left and not node.right:
            return bool(node.val)
        
        ## then 2 children
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        # 2 represents the boolean OR
        if node.val == 2:
            return left or right
        else:
            return left and right