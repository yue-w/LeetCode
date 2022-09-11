from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #return self.method1(nums, target)
        return self.method3(nums, target)
    
    def method1(self, nums, target):
        """
        DP (knapsack with hashing)
        """
        counter = {}
        counter[0] = 1
        
        for n in nums:
            counter_nxt = {}
            for c in counter:
                counter_nxt[c - n] = counter_nxt.get(c - n, 0) + counter[c]
                counter_nxt[c + n] = counter_nxt.get(c + n, 0) + counter[c]
            counter = counter_nxt
            

        return counter.get(target, 0)

    def method3(self, nums, target):
        """
        DFS, use prefixsum to prim.
        """
        def dfs(cur_sum, cur_idx):
            #print(cur_idx)
            if cur_idx == n:
                if cur_sum == target:
                    self.rst += 1
                return
            for i in range(cur_idx, n):
                dfs(cur_sum + nums[i], i + 1)
                dfs(cur_sum - nums[i], i + 1)
        
        self.rst = 0
        n = len(nums)
        memo = {}
        dfs(0, 0)
        return self.rst

if __name__ == '__main__':
    nums = [1,1,1,1,1]
    target = 3
    rst = Solution().findTargetSumWays(nums, target)
    print(rst)