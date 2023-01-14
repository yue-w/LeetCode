from typing import List

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        from collections import defaultdict
        counter = defaultdict(int)
        min_even = -1
        max_count = 0
        for n in nums:
            if n % 2:
                continue
            counter[n] += 1
            if (counter[n] > max_count) or ((counter[n] == max_count) and n < min_even):
                min_even = n
                max_count = counter[n]
            
        return min_even
            