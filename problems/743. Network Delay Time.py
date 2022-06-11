
import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #return self.method1(times, n, k)
        return self.method2(times, n, k)
        #return self.method3(times, n, k)
    
    def method1(self, times, n, k):
        """
        Dijkstra's algorithm. Do not compute distance from source to every point,
        just keep the longest time. 
        Time: O(Elog(E))
        Space: E
        """
        
        ## Build an adjacent list
        ## This problem is 1 indexed, so we add a dummy node 0 
        adlist = [[] for _ in range(n+1)]
        for time in times:
            tail, head, weight = time[0], time[1], time[2]
            adlist[tail].append((head, weight))

        visited = [0] * (n + 1)
        
        rst = 0
        
        ## Use a heap. Elements in the heap are tuples
        ## The first element of tuple is time, the second element of tuple is node
        hp = [(0, k)]

        while hp:
            time, tail = heapq.heappop(hp)
            if visited[tail]:
                continue
            visited[tail] = 1
            
            rst = max(rst, time)
            for head, weight in adlist[tail]:
                heapq.heappush(hp, (time + weight, head))
                
        ## check if every node has been visited (ignore dummy node 0)    
        for i in range(1, n+1):
            if visited[i] == 0:
                return -1

        else:
            return rst

    def method2(self, times, n, k):
        """
        Dijkstra's algorithm. Comput the time from the source to every point. 
        Output the largetst one. 
        Time: O(Elog(E))
        Space: E
        """
        adlist = [[] for _ in range(n+1)]
        for time in times:
            tail, head, weight = time[0], time[1], time[2]
            adlist[tail].append((head, weight))

        visited = [0] * (n + 1)

        time_from_source = [float('inf')] * (n + 1)
        
        #hp = [((float('inf')), i) for i in range(1, n + 1)]
        hp = [(0, k)]
        heapq.heapify(hp)
        while hp:
            delay_time, tail = heapq.heappop(hp)
            if visited[tail]:
                continue
            visited[tail] = 1
            time_from_source[tail] = delay_time
            
            for head, weight in adlist[tail]:
                if time_from_source[tail] + weight < time_from_source[head]:
                    heapq.heappush(hp, (time_from_source[tail] + weight, head))
        
        ## ignore the dummy node 0
        rst = max(time_from_source[1:])
        if rst == float('inf'):
            return -1
        else:
            return rst 
    
    def method3(self, times, n, k):
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