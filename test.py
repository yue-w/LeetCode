#%%
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node,curr):
            ## Base case
            if not node:
                return 0
            curr = curr*10 + node.val
            left = dfs(node.left, curr)
            right = dfs(node.right, curr)
            return curr + left + right
        return dfs(root, 0)
            



tn = TreeNode(1)
tn.left = TreeNode(2)
tn.right = TreeNode(3)

solution = Solution()
print(solution.sumNumbers(tn))