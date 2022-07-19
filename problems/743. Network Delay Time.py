
import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        return self.method1(times, n, k)
        #return self.method2(times, n, k)

    
    def method1(self, times, n, k):
        """
        Dijkstra's algorithm. 
        This is a template use case of Dijkstra's algorithm
        Time: O(Elog(E))
        Space: O(E)
        """
        ## build an adjacent list. [time, nxt]
        ## 1 indexed
        adj = [[] for _ in range(n + 1)]
        for i1, i2, time in times:
            adj[i1].append((time, i2))
        
        rsts = [-1] * (n + 1) ## 1 indexed
        
        ## heap is (time, index)
        hq = [(0, k)]
        heapq.heapify(hq)
        while hq:
            time, index = heapq.heappop(hq)
            if rsts[index] != -1:
                continue
            rsts[index] = time
            for dt, nxt in adj[index]:
                if rsts[nxt] != -1:
                    continue
                heapq.heappush(hq, (time+dt, nxt))
                
        for i in range(1, n + 1):
            if rsts[i] == -1:
                return -1
        return max(rsts)
    
    def method2(self, times, n, k):
        """
        Floyd's algorithm
        Time: O(n^3)
        """
        ## dp is a 2-D array, d[i][j] is the distance ("time" in this problem)
        ##  from node i to node j
        dp = [[float('inf') for _ in range(n)] for _ in range(n)]
        ## initialize dp. Notice that dp[i][i] is 0
        for i in range(n):
            dp[i][i] = 0
        for n1, n2, t in times:
            dp[n1-1][n2-1] = t
            
        for pivot in range(n):
            for i in range(n):
                for j in range(n):
                    dp[i][j] = min(dp[i][j], dp[i][pivot] + dp[pivot][j])
        
        maxt = max(dp[k-1][:])
        if maxt == float('inf'):
            return -1
        else:
            return maxt
        
    
            

if __name__ == '__main__':
    s = Solution()
    times = [[2,1,1],[2,3,1],[3,4,1]]
    n = 4
    k = 2
    # times = [[1,2,1]]
    # n = 2
    # k = 2
    rst = s.networkDelayTime(times, n, k)
    print(rst)