
from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        rst = self.recursion(1, n)
        return rst
    
    def recursion(self, left, right):
        ## base case 1:
        if left > right:
            return [None]
        
        ## base case 2:
        if left == right:
            node = TreeNode(left)
            return [node]
        
        rst = []
        for v in range(left, right + 1):
            ## left
            leftrst = self.recursion(left, v - 1)
            ## right
            rightrst = self.recursion(v + 1, right)
            for l in leftrst:
                for r in rightrst:
                    node = TreeNode(v)
                    node.left = l
                    node.right = r
                    rst.append(node)
        
        return rst


if __name__ == '__main__':
    n = 3
    rst = Solution().generateTrees(n)
    print(rst)