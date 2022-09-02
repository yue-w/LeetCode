from typing import List

import bisect
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        m = len(queries)
        
        nums.sort()
        
        prefixsum = [0] * n
        prefixsum[0] = nums[0]
        
        for i in range(1, n):
            prefixsum[i] = prefixsum[i - 1] + nums[i]
        
        rst = [0] * m
        
        for i in range(m):
            idx = bisect.bisect_right(prefixsum, queries[i])
            rst[i] = idx 
            
        return rst