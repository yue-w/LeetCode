
#%%
from typing import Optional
from tools import deserialize, drawtree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        depth = 0
        curr = root
        while curr:
            depth += 1
            curr = curr.left
        curr = [root]
        i = 1
        while i < depth:
            if i == 
            vals = []
            for node in curr:
                vals.append(node.left.val)
                vals.append(node.right.val)
            j = -1
            for node in curr:
                node.left.val = vals[j]
                node.right.val = vals[j - 1]
                j -= 2
            
            #curr = nxt
            i += 2

        return root

root = '[2,3,5,8,13,21,34]'

root = deserialize(root)
drawtree(root)
rst = Solution().reverseOddLevels(root)
drawtree(root)