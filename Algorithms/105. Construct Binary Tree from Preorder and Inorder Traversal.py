from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_dic = {inorder[i]:i for i in range(len(inorder))}

        def helper(left_preorder, right_preorder, left_inorder, right_inorder):
            """
            Build a tree with root
            """
            if left_preorder > right_preorder or left_inorder > right_inorder:
                return None
            root = TreeNode()
            root_val = preorder[left_preorder]
            root.val = root_val
            l_pre = left_preorder + 1
            r_pre = left_preorder + in_dic[root_val] - left_inorder 
            l_in = left_inorder
            r_in = in_dic[root_val] - 1
            root.left = helper(l_pre,r_pre,l_in,r_in)
            l_pre = r_pre + 1
            r_pre = right_preorder
            l_in = in_dic[root_val] + 1
            r_in = right_inorder
            root.right = helper(l_pre,r_pre,l_in,r_in)
            return root 

        return helper(0, len(preorder)-1, 0, len(inorder)-1)

if __name__ == '__main__':
    s = Solution()
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]

    rst = s.buildTree(preorder, inorder)
    print(rst.val)