
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.method1(root, low, high)
        #return self.method2(root, low, high)
    def method1(self, root, low, high):
        self.rst = 0

        def dfs(node):
            ## Base case
            if not node:
                return
            if node.val < low:
                dfs(node.right)
            elif node.val > high:
                dfs(node.left)
            else:
                self.rst += node.val
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return self.rst

    def method2(self, root, low, high):
        ## BFS
        from collections import deque
        dq = deque([root])
        rst = 0
        while dq:
            for _ in range(len(dq)):
                node = dq.popleft()
                if low <= node.val <= high:
                    rst += node.val
                    if node.left:
                        dq.append(node.left)
                    if node.right:
                        dq.append(node.right)
                if node.val < low:
                    if node.right:
                        dq.append(node.right)
                if node.val > high:
                    if node.left:
                        dq.append(node.left)
        return rst
        