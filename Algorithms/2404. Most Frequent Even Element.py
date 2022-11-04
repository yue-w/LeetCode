from typing import List

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        from collections import Counter
        counter = Counter(nums)
        keys = list(counter.keys())
        keys.sort()
        rst = -1
        for k in keys:
            if k % 2 == 0 and counter[k] > counter[rst]:
                rst = k
        return rst