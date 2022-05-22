
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        pre_nums = []
        self.dfs(root, pre_nums)
        return self.sum
    
    def dfs(self, node, pre_nums):
        ## Base case: leaf node
        if not node.left and not node.right:
            n = len(pre_nums)
            for i in range(n):
                self.sum += pre_nums[i] * 10**(n - i)
            self.sum += node.val
            return
        
        pre_nums_c = pre_nums[:]
        pre_nums_c.append(node.val)
        if node.left:
            self.dfs(node.left, pre_nums_c)
        if node.right:
            self.dfs(node.right, pre_nums_c)
        