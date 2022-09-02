from typing import List

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Reroot
        """
        # adjlist
        adjlist = [[] for _ in range(n)]
        for v1, v2 in edges:
            adjlist[v1].append(v2)
            adjlist[v2].append(v1)
        
        # step 1: counts the node of each subtree
        visited = [0] * n
        counts = [0] * n
        self.count_node(visited, adjlist, counts, 0)
        
        visited = [0] * n
        # step 2: use 0 as root, count total distance
        distances = [0] * n
        distances[0] = self.get_dis(adjlist, visited, distances, counts, 0)

        # step 3: compute the total distances for all the other nodes
        visited = [0] * n
        visited[0] = 1
        self.get_total_dis(adjlist, distances, visited, counts, 0, n)
            
        return distances

    def count_node(self, visited, adjlist, counts, node):
        """
        Count how many nodes are there with "node" as root (include root)
        """
        # base case
        if visited[node] != 0:
            return 0
        visited[node] = 1
        count = 1
        for nxt in adjlist[node]:
            count += self.count_node(visited, adjlist, counts, nxt)
        counts[node] = count    
        return count
    
    def get_dis(self, adjlist, visited, distances, counts, node):
        """
        Get total distance from node (root) to all the other nodes below
        """
        if visited[node] == 1:
            return 0
        visited[node] = 1
        tol_dis = 0
        for nxt in adjlist[node]:
            tol_dis += self.get_dis(adjlist, visited, distances, counts, nxt)
        ## all the nodes (other than the root) will add 1  
        tol_dis += counts[node] - 1
        return tol_dis
    
    def get_total_dis(self, adjlist, distances, visited, counts, node, n):
        """
        Get total distance
        """
        for nxt in adjlist[node]:
            if visited[nxt] != 0:
                continue
            visited[nxt] = 1
            b = counts[nxt]
            a = n - b
            distances[nxt] = distances[node] - b + a
            self.get_total_dis(adjlist, distances, visited, counts, nxt, n)
        
if __name__ == '__main__':
    n = 6
    edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
    rst = Solution().sumOfDistancesInTree(n, edges)
    print(rst)