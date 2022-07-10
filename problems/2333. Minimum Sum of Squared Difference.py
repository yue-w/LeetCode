from typing import List

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        k = k1 + k2
        n = len(nums1)
        diffs = [abs(nums1[i] - nums2[i]) for i in range(n)]
        
        diffs.sort(reverse=True)
        
        #### calculate prefixsum
        prefix = [0] * n
        prefix[0] = diffs[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + diffs[i]
        
        ## if k is large enough to make every number 0
        if prefix[n-1] <= k:
            return 0
        
        i = 0
        while (i < n and (prefix[i] - diffs[i] * (i + 1)) <= k):
            i += 1

        i -= 1
        ## now diffs[0] = diffs[1] = ... diffs[i] > diffs[i + 1]
        ## not enough k to go to nums[i+1], but may remain some value
        ## to make nums[0] to nums[i] even smaller (but still larger than
        ## nums[i + 1])
        remain = k - (prefix[i] - diffs[i] * (i + 1)) 
        reduce_each = remain // (i + 1)
        remainder = remain % (i + 1)
        
        rst = 0
        ## height (diffs[i] - reduce_each - 1), count is remainder
        rst += (diffs[i] - reduce_each - 1) * (diffs[i] - reduce_each - 1) * remainder
        
        ## height (), count is i + 1 - remainder
        rst += ((diffs[i] - reduce_each) * (diffs[i] - reduce_each)) * (i + 1 - remainder)
        
        ## height diffs[i]
        for index in range(i + 1, n):
            rst += diffs[index] * diffs[index]

        
        return rst
            
        
        