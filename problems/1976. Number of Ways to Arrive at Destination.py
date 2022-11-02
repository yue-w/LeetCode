from typing import List
import heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        if n <= 1:
            return 1
        M = int(1e9 + 7)
        
        adjlist = [[] for _ in range(n)]
        for i1, i2, time in roads:
            adjlist[i1].append((time, i2))
            adjlist[i2].append((time, i1))
        
        dis = [-1] * n
        
        hq = [(0, 0)]
        heapq.heapify(hq)
        ## Use Djistra's algorithm to get the shortest path from 0 to all other points
        while hq:
            t, c = heapq.heappop(hq)
            if dis[c] != -1:
                continue
            dis[c] = t
            
            ## add all of c's neighbors into heap
            for t2, c2 in adjlist[c]:
                if dis[c2] == -1:
                    heapq.heappush(hq, (t + t2, c2))

        ## now dis[i] is the shortest path from 0 to i
        
        memo = [-1] * n
        def dfs(city, remain):
            ## base case
            if remain != dis[city]:
                return 0
            
            if city == 0:
                return 1

            if memo[city] != -1:
                return memo[city]
            
            v = 0
            for d, c in adjlist[city]:
                v += dfs(c, remain - d)
                v %= M
            memo[city] = v
            return  v

        rst = dfs(n-1, dis[n-1])
        
        return rst % M