##Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #Use DFS (stack) to check each node, whether it can be the root of the sub root. Return early if found.
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            run_rst = self.compare(node, subRoot)
            if run_rst:
                return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False    
        
        
    def compare(self, root, subRoot):
        # Base case 1: one or both nodes are None
        if not root or not subRoot:
            return root == subRoot

        if root.val != subRoot.val:
            return False
        
        left = self.compare(root.left, subRoot.left)
        right = self.compare(root.right, subRoot.right)
        return left and right
        