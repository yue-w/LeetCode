from typing import List
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        """
        Ideas: 
        Sort,
        array of diff,
        Two pointers
        """
        ## corner case, len(nums) == 1
        if len(nums) == 1:
            return 1
        nums.sort()
        j = 1## 1?
        rst = 0
        for i in range(len(nums)):
            while j < len(nums) and (nums[j] == nums[i] or k >= (nums[j] - nums[j-1]) * (j - i)):
                k -= (nums[j] - nums[j-1]) * (j - i)
                j += 1
            rst = max(rst, j - i)
            ## update k
            k += nums[j-1] - nums[i]
            
        return rst