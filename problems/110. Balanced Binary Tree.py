
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Two things to check:
            whether each subtree is balanced
            whether the heights of two subtrees differed by 1 or less
        """
        left, right = self.dfs(root)
        return abs(left-right) <= 1

    def dfs(self, node):
        """
        Return the length of left and right sub tree.
        """
        ## base case 1. None
        if not node:
            return -1, -1
        
        left_left, left_right = self.dfs(node.left)
        ## if the left subtree is unbalanced already, return early
        if abs(left_left - left_right) > 1:
            return 0, float('inf')
        
        right_left, right_right = self.dfs(node.right)
        # if the right subtree is unbalanced already, regurn early
        if abs(right_left - right_right) > 1:
            return 0, float('inf')
        
        return 1+max(left_left, left_right), 1+max(right_left, right_right)