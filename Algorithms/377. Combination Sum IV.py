from typing import List
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        #return self.method1(nums, target)
        return self.method2(nums, target)
        
    def method1(self, nums, target):
        """
        DFS with memoization
        """
        def dfs(curr, target):
            ## base case
            if curr == target:
                return 1
            
            ## if in memo
            if curr in memo:
                return memo[curr]
            
            cur_sum = 0
            for i in range(len(nums)):
                if curr + nums[i] <= target:
                    cur_sum += dfs(curr + nums[i], target)
            memo[curr] = cur_sum
            return cur_sum

        ## memo[val]: how many ways to generate sum equals val        
        memo = {}
        return dfs(0, target)
    
    def method2(self, nums, target):
        """
        DP
        """
        DP = [0] * (target + 1)
        DP[0] = 1
        i = 1
        for i in range(1, target + 1):
            for n in nums:
                if i - n >= 0:
                    DP[i] += DP[i - n]
        
        
        return DP[target]
        

if __name__ == '__main__':
    nums = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    target = 10
    rst = Solution().combinationSum4(nums, target)
    print(rst)
        
        