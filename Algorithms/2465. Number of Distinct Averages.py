

class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        rst = set()
        hq1 = nums[:]
        heapq.heapify(hq1)
        hq2 = [-n for n in nums]
        heapq.heapify(hq2)
        while hq1:
            n1 = heapq.heappop(hq1)
            n2 = heapq.heappop(hq2)
            rst.add((n1 - n2)/2)
        
        
        return len(rst)