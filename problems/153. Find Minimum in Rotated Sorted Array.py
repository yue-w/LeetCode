


from typing import List 

class Solution:
    def findMin(self, nums: List[int]) -> int:
        ## if there is only 1 element, return it.
        ## if not rotated, return the first element.
        ## Two two conditions above are combined.
        if nums[0] <= nums[-1]:
            return nums[0]
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2

            if mid + 1 < len(nums):
                if nums[mid] > nums[mid + 1]:
                    return nums[mid + 1]

            if nums[left] < nums[mid]:
                left = mid
            else:
                right = mid
                
        return left
            
if __name__ == '__main__':

    s = Solution()
    nums = [2,3,4,5,1]
    print(s.findMin(nums))