
from typing import Optional

## Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        return self.bfs(root)
    
    def bfs(self, root):
        min_depth = 0
        dq = deque() ## keep entering from right (append()) and leaving from left (popleft())
        if root:
            dq.append(root)
        while dq:
            min_depth += 1
            len_cur = len(dq)
            ## process the current level
            for i in range(len_cur):
                node = dq.popleft()
                ## if find a leaf node, return
                if (not node.left) and (not node.right):
                    return min_depth
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
        
        return min_depth