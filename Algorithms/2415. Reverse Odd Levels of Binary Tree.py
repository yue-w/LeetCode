
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root.left:
            return root
    
        pre = [root]
        cur = [root.left, root.right]
        level = 1
        while cur:
            nxt = []
            if cur[0].left:
                for node in cur:
                    nxt.append(node.left)
                    nxt.append(node.right)
            if level % 2 == 1:
                cur.reverse()
                i = 0
                while i < len(pre):
                    pre[i].left = cur[2 * i]
                    pre[i].right = cur[2 * i + 1]
                    i += 1
                if cur[0].left:
                    j = 0
                    while j < len(cur):
                        cur[j].left = nxt[2 * j]
                        cur[j].right = nxt[2 * j + 1]
                        j += 1
            level += 1
            pre = cur
            cur = nxt
            
        return root