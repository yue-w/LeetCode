
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        #return self.method1(nums)
        return self.method2(nums) ## preferred method
    def method1(self, nums):
        """
        Binary search
        """
        left = 0
        right = len(nums) - 1
            
        ## if rotation times % len(nums) == 0
        if nums[left] < nums[right]:
            return nums[left]
        
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else: #nums[mid] == nums[right]
                right -= 1
            
        return nums[left]
    
    def method2(self, nums):
        ### remove points from the end
        while len(nums) > 1 and nums[0] == nums[-1]:
            nums.pop()
        
        ## now nums has at least 1 point
        if nums[0] < nums[-1]:
            return nums[0]
        
        ## if reaching this point, nums[0] > min[nums]
        left = 0
        right = len(nums) - 1
        target = nums[0]
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                left = mid + 1
            else:
                right = mid
        return nums[left]

if __name__ == '__main__':

    s = Solution()
    nums = [2,2,2,0,2,2,2]
    print(s.findMin(nums))