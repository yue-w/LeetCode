
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def dfs(node, target):
            """
            return node with leaf with target value removed
            """
            ## base case
            if not node:
                return None
            
            ## remove left subtrees
            node.left = dfs(node.left, target)
            
            ## remove right sub trees
            node.right = dfs(node.right, target)

            ## if after removing subtrees, this node becomes a leaf
            if (not node.left) and (not node.right) and (node.val == target):
                return None
            return node
        
        root = dfs(root, target)
        return root