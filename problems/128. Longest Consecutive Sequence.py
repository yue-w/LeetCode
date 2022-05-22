from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Time O(n)
        Space O(n)
        """
        rst = 0
        seen = {n for n in nums}
        
        while seen:
            counter = 1
            pivot = seen.pop()
            pivot_p = pivot + 1
            while pivot_p in seen:
                counter += 1
                seen.remove(pivot_p)
                pivot_p += 1
                
            pivot_m = pivot - 1
            while pivot_m in seen:
                counter += 1
                seen.remove(pivot_m)
                pivot_m -= 1
                
            rst = max(rst, counter)
            
            
        return rst