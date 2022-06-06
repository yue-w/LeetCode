from typing import List

from collections import defaultdict
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ## a hash store the first time (index) that the prefix sum 
        ## have this value
        seen = defaultdict(int)
        seen[0] = -1
        pre_sum = 0
        rst = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                pre_sum += 1
            else:
                pre_sum -= 1
            if pre_sum not in seen:
                seen[pre_sum] = i
            else:
                curr = i - seen[pre_sum]
                rst = max(rst, curr)
                
        return rst


"""
Prefixsum and hash. 
Add 1 if the number is 1, minus 1 if the number is 0
If a number is seen again, it means the sums in between is 0 (equal numbers of 0 and
1). Do not forget to add a 0 with index -1.
"""