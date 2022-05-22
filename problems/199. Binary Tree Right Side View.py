from typing import Optional, List

## Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #return self.bfs(root)
        return self.recursion(root)
    
    def bfs(self, root):
        rst = []
        dq = deque() ## Keep entering from right and leaving from left.
        if root:
            dq.append(root)
            while dq:
                len_curr = len(dq)
                for i in range(len_curr):
                    node = dq.popleft()
                    ## if node is the last one in this level, add it to rst
                    if i == len_curr - 1:
                        rst.append(node.val)
                    ## next level
                    if node.left:
                        dq.append(node.left)
                    if node.right:
                        dq.append(node.right)
        return rst

    def recursion(self, root):
        rst = []
        self._recursion(root, rst, 0)
        return rst
    
    def _recursion(self, root, rst, level):
        ## Base case
        if not root:
            return
        if level == len(rst):
            rst.append(root.val)
        self._recursion(root.right, rst, level + 1)
        self._recursion(root.left, rst, level + 1)
        