from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            """
            Return whether subtrees contain 1
            """
            ## base case None
            if not node:
                return False
            
            left = dfs(node.left)
            if not left:
                node.left = None
            right = dfs(node.right)
            if not right:
                node.right = None
                
            return left or right or node.val
        
        contains_one = dfs(root)
        if contains_one:
            return root
        return None

if __name__ == '__main__':
    root = TreeNode(0)
    root.right = TreeNode(0)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(0)
    rst = Solution().pruneTree(root)
    print(rst.val)