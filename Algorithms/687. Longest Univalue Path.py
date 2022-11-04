##Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.rst = 0
        self.dfs(root)
        return self.rst
    

    def dfs(self, node):
        ## base case:
        if not node:
            return 0
        
        left = self.dfs(node.left)
        if node.left:
            if node.left.val == node.val:
                left += 1
            else:
                left = 0
        
        right = self.dfs(node.right)
        if node.right:
            if node.right.val == node.val:
                right += 1
            else:
                right = 0
        
        self.rst = max(self.rst, left + right)
        return max(left, right)
        


node = TreeNode(5)
node.left = TreeNode(4)
node.right = TreeNode(5)
node.left.left  = TreeNode(1)
node.left.right  = TreeNode(1)
node.right.right = TreeNode(5)
print(Solution().longestUnivaluePath(node))