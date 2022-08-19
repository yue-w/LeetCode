from typing import List
from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        """
        time: O(nlogn)
        Space: O(n)
        """
        counter = Counter(arr)
        counts = list(counter.values())
        counts.sort(reverse=True)
        accumulator = 0
        i = 0
        while accumulator < len(arr) / 2:
            accumulator += counts[i]
            i += 1
            
        return i