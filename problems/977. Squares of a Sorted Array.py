from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        rst = []
        left, right = 0, len(nums) - 1
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                rst.append(nums[left] ** 2)
                left += 1
            else:
                rst.append(nums[right] ** 2)
                right -= 1
        
        rst.reverse()
        return rst
    