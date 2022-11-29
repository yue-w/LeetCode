

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        DFS
        """
        def dfs(node, cur_max):
            ## base case
            if not node:
                return
            if node.val >= cur_max:
                self.rst += 1
                cur_max = node.val
            dfs(node.left, cur_max)
            dfs(node.right, cur_max)
            
        self.rst = 0
        dfs(root, float('-inf'))
        return self.rst