
from typing import List
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        """
        Binary search, heap
        """
        import heapq
        rst = 0
        intervals.sort()
        hq = []
        for a, b in intervals:
            if not hq:
                heapq.heappush(hq, b)
            else:
                if a > hq[0]:
                    heapq.heappushpop(hq, b)
                else:
                    heapq.heappush(hq, b)
            rst = max(rst, len(hq))
        
        
        return rst
        
        