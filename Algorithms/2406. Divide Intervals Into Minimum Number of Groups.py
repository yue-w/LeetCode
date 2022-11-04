
from typing import List

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        #return self.method1(intervals)
        return self.method2(intervals)
    
    def method1(self, intervals):
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
    
    def method2(self, intervals):
        """
        Sweeping line
        """
        stamps = []
        for a, b in intervals:
            stamps.append((a, 1))
            stamps.append((b, -1))
        stamps.sort(key=lambda x: (x[0], -x[1]))
        count = 0
        rst = 0
        for time, v in stamps:
            count += v
            rst = max(rst, count)
        return rst
        
        