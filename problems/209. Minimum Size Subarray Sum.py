
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Sliding window a slow and a fast pointer, right pointer to explore (find a solution) and left pointer to shink (find minimum size) 
        """
        
        
        found = False
        min_len = len(nums) + 1
        
        left = 0
        curr_sum = 0
        
        for right in range(len(nums)):
            curr_sum += nums[right]
            ## if not less than target
            if curr_sum >= target:
                found = True
                while left <= right:
                    ## if throw away nums[left] still not less than target, then shrink
                    if curr_sum - nums[left] >= target:
                        curr_sum -= nums[left]
                        left += 1
                    else:
                        break
                ## update min_len
                min_len = min(min_len, right - left + 1)
                        
                    
        
        
        if not found:
            return 0
        else:
            return min_len
        
        
"""
Test cases
    Corner case 1:
    empty array
    Corner case 2:
    1 elements and satisfy
    1 elements and not satisfy
    Normal cases
    Does not exist: return 0
    Exist: return min_val
"""