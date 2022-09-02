
from typing import List
import heapq
class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        """
        Reference: https://youtu.be/pquoywwK0_w
        """
        maxsum = 0
        for num in nums:
            if num > 0:
                maxsum += num
        
        if k == 1:
            return maxsum
        
        absv = [abs(num) for num in nums]
        absv.sort()
        
        hq = []
        heapq.heappush(hq, (absv[0], 0))
        rst = maxsum
        counter = 0
        for i in range(k-1):
            curr, idx = heapq.heappop(hq)
            if i == k - 2:
                return maxsum - curr
            if idx + 1 < len(absv):
                heapq.heappush(hq, (curr - absv[idx] + absv[idx + 1], idx + 1))
                heapq.heappush(hq, (curr + absv[idx + 1], idx + 1))
        
        return -1