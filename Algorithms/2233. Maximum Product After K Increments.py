from typing import List

class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        """
        Time: O(nlogn)
        Space: O(1)
        """
        M = int(1e9+7)
        nums.sort()
        remain = k
        i = 0
        ## 0 to i (inclusive) have the same height nums[i]
        while i < len(nums) - 1 and remain - (i + 1) * (nums[i+1] - nums[i]) > 0:
            remain -= (i + 1) * (nums[i+1] - nums[i])
            i += 1
        height = nums[i]
        
        dh = remain // (i + 1)
        first = remain % (i + 1)
        rst = ((height + dh + 1) ** first) * ((height + dh) ** ((i + 1) - first))

        while i < len(nums) - 1:
            rst *= nums[i + 1]
            i += 1
            
        return rst % M
            

            
                
            