
from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        for i in range(N):
            if nums[i] < 0:
                nums[i] = 0
            
        for i in range(N):
            val = abs(nums[i])
            if 1 <= val <= N:
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    nums[val - 1] = - (N + 1)


        for i in range(N):
            if nums[i] >= 0:
                return i + 1
        return N + 1

if __name__ == '__main__':
    s = Solution()
    nums = [7,8,9,11,12]
    print(s.firstMissingPositive(nums))
            
