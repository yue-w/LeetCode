

#%%
from collections import deque
#%% 
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        #return self.method1(node)
        return self.method2(node)
    
    def method1(self, node):
        """
        DFS
        """
        if not node:
            return None
        visited = {}

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
    
    
    def method2(self, node):
        """
        BFS
        """
        if not node:
            return None
        
        ## the node may be connected by multiple other nodes 
        ## In BFS, a node may be encountered multiple times.
        ## Use a hashmap to map from node.val to node.
        ## if a node is not visited for the first time, use the recorded copy.
        ## This makes sure there is only one copy of each node, its neighbors are
        ## are updated in the iteration process.
        visited = {}
        
        dq = deque() ## enter from right, leave from left
        dq.append(node)
        while dq:
            for _ in range(len(dq)):
                cur_node = dq.popleft()
                ## if the node has been visited, get it from the hash map
                if cur_node.val in visited:
                    cur_node_cp = visited[cur_node.val]
                ## if the node has not been visited, make a deep copy, and save
                ## it in the hash map.
                else:
                    cur_node_cp = Node(cur_node.val)
                for n in cur_node.neighbors:
                    ## if node n has not been visited, make a deep copy of this node
                    ## and add it to the neighbour list.
                    if not n.val in visited:
                        ## if the node has not been visited, add it to queue
                        dq.append(n)
                        n_cp = Node(n.val)
                        cur_node_cp.neighbors.append(n_cp)
                        visited[n_cp.val] = n_cp
                    ## if n has been visited before, a copy is already created,
                    ## and it is stored in the hash map.
                    else:
                        cur_node_cp.neighbors.append(visited[n.val])
                if not cur_node.val in visited:
                    visited[cur_node_cp.val] = cur_node_cp
                    
                    
        return visited[1]


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

    visited = set()
    def print_dfs(node):
        if node.val in visited:
            return
        visited.add(node.val)
        print(node.val)
        for n in node.neighbors:
            if n not in visited:
                print_dfs(n)

    print_dfs(ans)