import heapq
from typing import List

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        
        hq = [] # heap. elements: score, index, direction
        n = len(costs)
        left = candidates
        right = n - candidates
        
        ## left
        for i in range(left):
            heapq.heappush(hq, (costs[i], i, 1))
        
        ## right
        for i in range(max(left, right), n):
            heapq.heappush(hq, (costs[i], i, -1))
            
        right -= 1
        
        rst = 0
        for i in range(k):
            c, idx, dirc = heapq.heappop(hq)
            rst += c
            
            if left <= right:
                if dirc == 1:
                    heapq.heappush(hq, (costs[left], left, 1))
                    left += 1
                else:
                    heapq.heappush(hq, (costs[right], right, -1))
                    right -= 1
        
        return rst