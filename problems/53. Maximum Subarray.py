class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.method_2(nums)

                
            
    def method_1(self,nums):
        """
        Runtime: O(n)
        Space: O(n)
        """
        if len(nums) == 1:
            return nums[0]
        cum_sum = [0] * len(nums)
        cum_sum[0] = nums[0]
        for i in range(1, len(nums)):
            if nums[i] + cum_sum[i-1] >  nums[i]:
                cum_sum[i] = nums[i] + cum_sum[i-1]
            else:
                cum_sum[i] = nums[i]
        return max(cum_sum)
    
    def method_2(self, nums):
        """
        Runtime: O(n),
        Space: O(1)
        """
        ans = nums[0]
        cumsum = nums[0]
        for i in range(1, len(nums)):
            cumsum = max(nums[i] + cumsum, nums[i]) 
            ans = max(ans, cumsum)
        return ans