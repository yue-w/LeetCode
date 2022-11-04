
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        """
        BFS
        """
        from collections import defaultdict, deque
        stack = [root]
        adjlist = defaultdict(list)
        #### step 1 build the graph
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
                adjlist[node.val].append(node.left.val)
                adjlist[node.left.val].append(node.val)
            if node.right:
                stack.append(node.right)
                adjlist[node.val].append(node.right.val)
                adjlist[node.right.val].append(node.val)
        
        #### step 2 BFS
        dq = deque()
        visited = set()
        dq.append(start)
        time = -1
        while dq:
            time += 1
            for _ in range(len(dq)):
                node = dq.pop()
                visited.add(node)
                for nxt in adjlist[node]:
                    if not nxt in visited:
                        visited.add(nxt)
                        dq.appendleft(nxt)
        return time