from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # #### Recursion
        # left = 0
        # right = len(nums) - 1
        # return self.recursion(nums, target, left, right)

        #### Iteration
        return self.iteration(nums, target)

    
    def recursion(self, nums, target, left, right):
        ## Base case
        if left > right:
            return - 1
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1 
        else:
            right = mid - 1
        return self.recursion(nums, target, left, right)

    def iteration(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1




if __name__ == '__main__':
    s = Solution()
    nums = [-1,0,3,5,9,12]
    target = 13
    print(s.search(nums, target))
    