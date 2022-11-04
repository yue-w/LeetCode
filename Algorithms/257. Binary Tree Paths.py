from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        #return self.method1(root)
        return self.method2(root)

    def method1(self, node):
        """
        DFS. 
        Check whether a node is None in the base case.
        """
        self.rst = []
        curr = []
        self.dfs(node, curr)
        return self.rst
    
    def dfs(self, node, curr):
        ## base case 1: None
        if not node:
            return
        ## base case 2: if leaf
        if not node.left and not node.right:
            curr.append(node)
            ## add curr to result
            temp = []
            for i in range(len(curr)):
                temp.append(str(curr[i].val))
                temp.append('->')
            if temp[-1] == '->':
                temp.pop()
            self.rst.append(''.join(temp))
            ## back track
            curr.pop()
            return
        
        ## recursion
        curr.append(node)
        self.dfs(node.left, curr)
        
        self.dfs(node.right, curr)
        ## back track
        curr.pop()

        
    def method2(self, node):
        """
        DFS 2.
        Check whether a node is None before going into dfs.
        """
        if not node:
            return []
        self.rst = []
        curr = []
        self.dfs2(node, curr)
        return self.rst

    def dfs2(self, node, curr):
        """
        node will not be None, the check is done before going into dfs.
        """
        ## base case: leaf
        if not node.left and not node.right:
            curr.append(str(node.val))
            self.rst.append(''.join(curr))
            curr.pop()
            return 

        curr.append(str(node.val))
        if node.left:
            curr.append('->')
            self.dfs2(node.left, curr)
            curr.pop()
        if node.right:
            curr.append('->')
            self.dfs2(node.right, curr)
            curr.pop()
        curr.pop()

        
        

        


        

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    rst = Solution().binaryTreePaths(root)
    print(rst)