from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def dfs(node, val):
            # Base case ?
            if val > node.val:
                if not node.right:
                    node.right = TreeNode(val)
                    return
                else:
                    dfs(node.right, val)
            else: #val < node.val
                if not node.left:
                    node.left = TreeNode(val)
                    return
                else:
                    dfs(node.left, val)

        if not root:
            return TreeNode(val)
        dfs(root, val)
        return root