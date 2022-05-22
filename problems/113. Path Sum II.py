from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        rst = []
        path = []
        self.dfs(root, targetSum, path, rst)
        return rst
        
    def dfs(self, node, remain, path, rst):
        ## Base case: None
        if not node:
            return 
        ## Base case: leaf node
        if not node.left and not node.right:
            if remain - node.val == 0:
                path.append(node.val)
                rst.append(path)
            return 
        
        if node.left:
            path_c = path[:]
            path_c.append(node.val)
            self.dfs(node.left, remain - node.val, path_c, rst)
        if node.right:
            path_c = path[:]
            path_c.append(node.val)
            self.dfs(node.right, remain - node.val, path_c, rst)