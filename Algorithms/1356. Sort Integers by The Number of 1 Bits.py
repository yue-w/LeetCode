
from typing import List
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def bit_count_one(n):
            count = 0
            while n:
                count += 1
                n &= n - 1
            return count
        array = [(bit_count_one(a), a) for a in arr]
        array.sort()
        return [a[1] for a in array]