from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # ## Method 1: time O(n^2)
        # root = self.recursion(preorder, inorder)
        # return root
        
        ## Mehod 2: time O(n)
        dic = {v:i for i, v in enumerate(inorder)}
        root = self.recursion_hash(preorder, inorder, dic, 0, len(preorder)-1, 0, len(inorder) - 1)
        return root
    
    
    def recursion_hash(self, preorder, inorder, dic, pre_start, pre_end, in_start, in_end):
        """
        time: O(n)
        space: O(n)
        """
        # pre_end - pre_start = in_end - in_start
        ## Base case
        if pre_end < pre_start:
            return None 
        root = TreeNode(preorder[pre_start])

        in_start_left = in_start
        in_end_left = dic[root.val] - 1

        in_start_right  = dic[root.val] + 1
        in_end_right = in_end

        pre_start_left = pre_start + 1
        pre_end_left = pre_start_left + (in_end_left - in_start_left) ## preorder and inorder have same length

        pre_start_right = pre_end_left + 1
        pre_end_right =  pre_end

        root.left = self.recursion_hash(preorder, inorder, dic, pre_start_left, pre_end_left, in_start_left, in_end_left)
        root.right = self.recursion_hash(preorder, inorder, dic, pre_start_right, pre_end_right, in_start_right, in_end_right)

        return root
        
    def recursion(self, preorder, inorder):
        """
        return head of the sub tree
        time: O(n^2)
        space: O(1)
        """
        #assert len(preorder) == len(inorder)
        ## Base case: preorder and inorder is empty
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        root_index = inorder.index(root.val) #dic[root.val]

        root.left = self.recursion(preorder[1: root_index + 1], inorder[:root_index])
        root.right = self.recursion(preorder[root_index + 1:], inorder[root_index + 1:])
        
        return root

if __name__ == '__main__':
    s = Solution()
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]

    rst = s.buildTree(preorder, inorder)
    print(rst.val)