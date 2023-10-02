class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        """
        Two pointers
        """
        rst = 1
        i = 0
        j = 1
        while j < len(nums):
            if nums[j] > nums[j - 1]:
                rst = max(rst, j - i  + 1)
            else:
                i = j
            j += 1

        return rst