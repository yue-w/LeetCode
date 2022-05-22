



#%% 
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        """
        DFS, hash
        """
        if not node:
            return None
        visited = {}
        #node_copy = Node(node.val)
        node_copy = self.dfs(node, visited)
        return node_copy
        
    def dfs(self, node, visited):
        if node.val in visited:
            return visited[node.val]
        
        node_copy = Node(node.val)
        visited[node.val] = node_copy
        for n in node.neighbors:
            n_cp = self.dfs(n, visited)
            node_copy.neighbors.append(n_cp)
            
        return node_copy
#%%
if __name__ == '__main__':

    s = Solution()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    # [[2,4],[1,3],[2,4],[1,3]]
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

    ans = s.cloneGraph(node1)

# %%
