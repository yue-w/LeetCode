
import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Clarification: multiple paths to a node? If multiple paths are possible, use the smallest time?
        """
        self.build_graph(times, n)
        t = [float('inf')] * n
        visited = set()
        
        #hp = [((float('inf')), i) for i in range(1, n + 1)]
        hp = [(0, k-1)]
        heapq.heapify(hp)
        while hp:
            weight, tail = heapq.heappop(hp)
            if tail in visited:
                continue
            visited.add(tail)
            t[tail] = weight
            for head, weight in self.adlist[tail]:
                if t[tail] + weight < t[head]:
                    heapq.heappush(hp, (t[tail] + weight, head))
                

        if len(visited) < n:
            return -1
        else:
            return max(t)
        
    def build_graph(self, times, n):
        self.adlist = [[] for _ in range(n)]
        for time in times:
            tail, head, weight = time[0], time[1], time[2]
            self.adlist[tail-1].append((head-1, weight))
            

if __name__ == '__main__':
    s = Solution()
    times = [[2,1,1],[2,3,1],[3,4,1]]
    n = 4
    k = 2
    rst = s.networkDelayTime(times, n, k)
    print(rst)