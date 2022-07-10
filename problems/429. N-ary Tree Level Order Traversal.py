
from typing import List
## Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


from collections import deque

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        #return self.method1(root) ## bfs
        #return self.method2(root) ## dfs uising recursion
        return self.method3(root) ## dfs using stack
    
    def method1(self, root):
        """
        BFS
        """
        rst = []
        dq = deque() ## Keep entering form right (append()) and leaving from left (popleft())
        if root:
            dq.append(root)
        while dq:
            curr = []
            cur_len = len(dq)
            for i in range(cur_len):
                node = dq.popleft()
                curr.append(node.val)
                ## add children to the next level
                for c in node.children:
                    dq.append(c)
            rst.append(curr)

        return rst
    
    def method2(self, root):
        """
        DFS with recursion
        """
        if not root:
            return []
        
        def dfs(root, rst, level):
            ## base case
            if not root:
                return
            if level == len(rst):
                rst.append([root.val])
            else:
                rst[level].append(root.val)
            
            for c in root.children:
                dfs(c, rst, level + 1)
        
        rst = []
        dfs(root, rst, 0)
        return rst
    
    def method3(self, root):
        """
        DFS using stack
        """
        if not root:
            return []
        
        rst = []
        stack = []
        stack.append((root, 0))
        while stack:
            node, level = stack.pop()
            if level == len(rst):
                rst.append([node.val])
            else:
                rst[level].append(node.val)
            
            for c in node.children[::-1]:
                stack.append((c, level + 1))
        
        return rst
                
            
        
        
        
        
        
        
        
        
        

