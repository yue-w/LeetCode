
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero, two, curr = -1, len(nums), 0
        while curr < two:
            if nums[curr] == 1:
                curr += 1
                continue
            elif nums[curr] == 2:
                two -= 1
                nums[two], nums[curr] = nums[curr], nums[two]
            else: ## 0
                zero += 1
                nums[zero], nums[curr] = nums[curr], nums[zero]
                curr += 1




if __name__ == '__main__':
    s = Solution()
    nums = [2,1,2]
    s.sortColors(nums)
    print(nums)