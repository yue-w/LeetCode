from typing import List, Optional

## Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return self.bfs(root)
    
    def bfs(self, root):
        rst = []
        dq = deque() ## enter from right, left from left
        left2right = True
        if root:
            dq.append(root)
            
        while dq:
            len_cur = len(dq)
            cur_lev = []

            for i in range(len_cur):
                node = dq.popleft()
                cur_lev.append(node.val)
                ## add next level
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            if not left2right:
                cur_lev.reverse()
            left2right = not left2right
            rst.append(cur_lev)

        return rst