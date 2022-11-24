from typing import List
from collections import deque

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        
        def bobp(bob_path):
            """
            DFS to find the path from bob to root
            bob_path: (node index, steps to reach this node)
            """
            ## base case: reaches root
            if bob_path[-1] == 0:
                return True

            curr = bob_path[-1]
            for nxt in adjlist[curr]:
                if nxt in visited:
                    continue
                visited.add(nxt)
                bob_path.append(nxt)
                found = bobp(bob_path)
                if found:
                    return True
                ## backtracking
                bob_path.pop()
            return False
        
        # def dfs():
        n = len(edges) + 1
        adjlist = [[] for _ in range(n)] # if node i is a leaf, then len(adjlist[i]) == 1
        ## build the adjlist
        for n1, n2 in edges:
            adjlist[n1].append(n2)
            adjlist[n2].append(n1)
        
        ## dfs to find bob's path
        bob_path = [bob]
        visited = set([bob])
        bobp(bob_path)
        ## build a dictionary to record when did bob reach node i
        bobs = {bob_path[i]:i for i in range(len(bob_path))}
        
        ## BFS for alice
        rst = float('-inf')
        dq = deque([(0, 0)])
        steps_a = -1
        visited = set()
        while dq:
            steps_a += 1
            for _ in range(len(dq)):
                node, cur_v = dq.popleft()
                #print(node, cur_v)
                if node in visited:
                    continue
                visited.add(node)
                if node in bobs:
                    ## to split incom/cost with bob
                    steps_b = bobs[node]
                    if steps_a == steps_b:
                        cur_v += (amount[node])/2
                    elif steps_a < steps_b:
                        cur_v += amount[node]
                else:
                    cur_v += amount[node]
                
                if len(adjlist[node]) == 1 and node != 0:
                    rst = max(rst, cur_v)

                for nxt in adjlist[node]:
                    dq.append((nxt, cur_v))
 
        return int(rst)
        
if __name__ == '__main__':
    edges = [[0,1],[1,2],[2,3]]
    bob = 3
    amount = [-5644,-6018,1188,-8502]
    # edges = [[0,1],[1,2],[1,3],[3,4]]
    # bob = 3
    # amount = [-2,4,2,-4,6]
    rst = Solution().mostProfitablePath(edges, bob, amount)
    print(rst)