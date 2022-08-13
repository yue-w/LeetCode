from typing import List
class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        """
        Two pointers
        """
        rst = set()
        
        for i in range(len(nums)):
            curr = 0
            j = i
            while j < len(nums) and curr <= k:
                if nums[j] % p == 0:
                    curr += 1
                if 0 <= curr <= k:
                    rst.add(tuple(nums[i:j+1]))
                j += 1

        return len(rst)