##from sets import Set
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #n = len(nums)
        total = 0
        seenSum = {}
        seenSum[0] = 1
        runningSum = 0
        for i, n in enumerate(nums):
            runningSum += n
            key = runningSum - k
            
            total += seenSum.get(key, 0)
            ## update dictionary
            seenSum[runningSum] = seenSum.get(runningSum, 0) + 1
        return total
            
nums = [1,1,1]
k = 2
print(Solution().subarraySum(nums,k))