from typing import Optional, List
from collections import deque
from tools import drawtree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, curr, cursum):
            ## Base case
            if not node:
                return 
            curr.append(node.val)
            cursum += node.val
            ## If leaf
            if (not node.left) and (not node.right) and (cursum == targetSum):
                rst.append(curr[:])
                return
            
            dfs(node.left, curr, cursum)
            dfs(node.right, curr, cursum)
            curr.pop()

        if not root:
            return []
        rst = []
        dfs(root, [], 0)
        return rst

root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(1)
root.right = TreeNode(3)
root.right.right = TreeNode(2)

test = Solution().pathSum(root, 10)
print(test)
"""
    5
  4   3
1       2
"""
