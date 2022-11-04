
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        #return self.iteration(root, low, high)
        return self.recursion(root, low, high)
    
    def recursion(self, root, low, high):
        self.total = 0
        self.recursion_helper(root,low, high)
        return self.total
    
    def recursion_helper(self, root, low, high):
        ## base case:
        if not root:
            return
        if low <= root.val <= high:
            self.total += root.val
            self.recursion_helper(root.left, low, high)
            self.recursion_helper(root.right, low, high)
        elif root.val < low:
            self.recursion_helper(root.right, low, high)
        else:
            self.recursion_helper(root.left, low, high)
    
    def iteration(self, root, low, high):
        stack = [root]
        total = 0
        while stack:
            node = stack.pop()
            if low <= node.val <= high:
                total += node.val
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            if node.val < low:
                if node.right:
                    stack.append(node.right)
            if node.val > high:
                if node.left:
                    stack.append(node.left)
            
        return total
        