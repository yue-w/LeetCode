import math
from typing import List
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        """
        total: math.comb(n, 2)
        j - i != nums[j] - nums[i] <=> j - nums[j] != i - nums[i],
        so we only need to cauculate total pairs minus how many pairs satisfy (j - nums[j] == i - nums[i])
        
        """
        from collections import Counter
        n = len(nums)
        total = math.comb(n, 2)
        diff = [nums[i] - i for i in range(len(nums))]
        counter = Counter(diff)
        same = 0
        for value, count in counter.items():
            if count > 1:
                same += math.comb(count,2)
        return total - same