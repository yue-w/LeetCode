
from typing import List
from collections import Counter
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        ct = Counter(nums)
        v1 = 0
        v2 = 0
        for val in ct.values():
            v1 += val // 2
            v2 += val % 2
            
        return [v1, v2]