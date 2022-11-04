from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def dfs(node, dirs, value):
            # base case
            if not node:
                return False
            if node.val == value:
                return True
            if node.left:
                dirs.append('L')
                if dfs(node.left, dirs, value):
                    return True
                dirs.pop()
            if node.right:
                dirs.append('R')
                if dfs(node.right, dirs, value):
                    return True
                dirs.pop()
            return False
        
        left_path = []
        right_path = []
        dfs(root, left_path, startValue)
        dfs(root, right_path, destValue)
        i = 0
        while i < len(left_path) and i < len(right_path) and left_path[i] == right_path[i]:
            i += 1
        rst = ['U' for _ in range(i, len(left_path))]
        rst += right_path[i:]
        rst = ''.join(rst)
        return rst
        



if __name__ == '__main__':
    from tools import deserialize, drawtree
    root = '[5,1,2,3,null,6,4]'
    root = deserialize(root)
    startValue = 3
    destValue = 6
    rst = Solution().getDirections(root, startValue, destValue)
    print(rst)
    