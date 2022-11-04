
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        ## first and second node swaped
        self.first = None
        self.second = None
        ## record the previous node
        self.pre = TreeNode(float('-inf'))
        self.dfs(root)
        
        self.first.val, self.second.val = self.second.val, self.first.val
        
        
    def dfs(self, node):
        """
        In order traversal
        """
        ## base case
        if not node:
            return
        
        ## left
        self.dfs(node.left)
        
        ## do something
        ## if increasing is violated
        if node.val < self.pre.val:
            if not self.first:
                self.first = self.pre
                self.second = node
                self.pre = node
            else:
                self.second = node
                return
        else: ## no violation
            self.pre = node
            
            
        ## right
        self.dfs(node.right)
        