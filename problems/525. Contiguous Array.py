from typing import List

from collections import defaultdict
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """
        Prefixsum, add 1 if 1, subtract 1 if 0
        use a hash map to record the first time (index) of a prefixsum.
        If two indexes have the same prefixsum, there are equal 1 and 0 in between.
        """
        rst = 0
        presum = 0
        ## the first time seen 0 is at -1.
        first_seen_pos = {0:-1}
        for i in range(len(nums)):
            if nums[i] == 0:
                presum -= 1
            else:
                presum += 1
            if presum in first_seen_pos:
                rst = max(rst, i - first_seen_pos[presum])
            else:
                first_seen_pos[presum] = i
        return rst


"""
Prefixsum and hash. 
Add 1 if the number is 1, minus 1 if the number is 0
If a number is seen again, it means the sums in between is 0 (equal numbers of 0 and
1). Do not forget to add a 0 with index -1.
"""