from typing import List

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # rst = []
        # self.recursion(root, rst)
        # return rst
        return self.iteration(root)
    
    def recursion(self, node, rst):
        # base case: leaf node
        if not node:
            return
        self.recursion(node.left, rst)
        rst.append(node.val)
        self.recursion(node.right, rst)

    def iteration(self, root):
        rst = []
        stack = []
        pointer = root
        while pointer or stack:
            while pointer:
                stack.append(pointer)
                pointer = pointer.left
            pointer = stack.pop()
            rst.append(pointer.val)
            pointer = pointer.right
        return rst

if __name__ == '__main__':
    """
                a
            /       \
          b           c   
         / \         / \ 
       d     e      f    g 
    """
    root = TreeNode('a')
    root.left = TreeNode('b')
    root.left.left = TreeNode('d')
    root.left.right = TreeNode('e')
    root.right = TreeNode('c')
    root.right.left = TreeNode('f')
    root.right.right = TreeNode('g')
    
    s = Solution()
    rst = s.inorderTraversal(root)
    print(rst) 