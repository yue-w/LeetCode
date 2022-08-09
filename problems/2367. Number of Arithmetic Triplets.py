from typing import List
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        rst = 0
        seen = set(nums)
        for i in range(len(nums)):
            if (nums[i] + diff) in seen and (nums[i] + 2 *diff) in seen:
                rst += 1
        return rst