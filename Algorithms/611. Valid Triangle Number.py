from typing import List



class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """
        Sort the array? then three pointers?
        """
        if len(nums) < 3:
            return 0
        count = 0
        nums.sort()
        for k in range(len(nums) - 1, 1, -1):
            i = 0
            j = k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    count += (j - 1) - i + 1
                    j -= 1
                else:
                    i += 1
        return count

if __name__ == '__main__':
    s = Solution()
    nums = [4,2,3,4]
    rst = s.triangleNumber(nums)
    print(rst)