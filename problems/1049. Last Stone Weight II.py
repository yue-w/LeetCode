
from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        """
        Think about the whole colliding process as adding '+' or '-'
        sign in front of each number. The final result is the (non-negative) smallest of
        all the sum of these signed numbers. This transforms the problem to
        the knapsack problem. 
        dp = [set() for _ in range(len(nums))]
        and dp[i] is all possible sum values computed from nums[0:i+1] (with signes added).
        The transition function is dp[i] = {dp[j-1] + nums[j], dp[j-1] - nums[j]} for j = 1, 2... len(dp[i-1])
        Very similar to 494. Target Sum
        """
        currset = set([0])
        
        for w in stones:
            nxtset = set()
            for v in currset:
                nxtset.add(v + w)
                nxtset.add(v - w)
            currset = nxtset
            
        rst = float('inf')
        for v in currset:
            if v >= 0:
                rst = min(rst, v)
                if rst == 0:
                    return 0
                
        return rst