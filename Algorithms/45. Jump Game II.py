

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        
        N = len(nums)
        if N == 1:
            return 0
        
        start = 0
        end = 0
        steps = 0
        while start <= end:
            new_end = end
            for i in range(start, end + 1):
                new_end = max(new_end, i + nums[i])
                if new_end >= N - 1:
                    return steps + 1
            steps += 1
            start = end + 1
            end = new_end
            
            
        return -1
                
    