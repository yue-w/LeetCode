from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        self.rst = []
        self.target = targetSum
        curr = [root.val]
        
        self.dfs(root, curr, root.val)
        return self.rst
    
    def dfs(self, node, curr, cursum):
        ## base case: leaf node
        if not node.left and not node.right:
            if cursum == self.target:
                self.rst.append(curr[:])
            return
        
        if node.left:
            curr.append(node.left.val)
            self.dfs(node.left, curr, cursum+node.left.val)
            ## backtracking 
            curr.pop()
            
        if node.right:
            curr.append(node.right.val)
            self.dfs(node.right, curr, cursum+node.right.val)
            ## backtracking
            curr.pop()