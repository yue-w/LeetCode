


from typing import List 

class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Find the first element of the second half
        if nums[mid] > nums[0], the target is in the second half, so left = mid + 1
        if nums[mid] <= nums[0], the target is in the first half (or maby mid), so right = mid 
        """
        left = 0
        right = len(nums) - 1
        ## if not rotated, return the first element
        if nums[left] < nums[right]:
            return nums[left]
        
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= nums[0]:
                left = mid + 1
            else:
                right = mid
            
        return nums[left]

if __name__ == '__main__':

    s = Solution()
    nums = [4,5,6,7,0,1,2]
    print(s.findMin(nums))