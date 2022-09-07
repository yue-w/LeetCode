from functools import cache
import math
class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        #return self.method1(startPos, endPos, k)
        #return self.method2(startPos, endPos, k) # preferred method
        return self.method3(startPos, endPos, k)
    def method1(self, startPos, endPos, k):
        """
        DFS with memo
        """
        def dfs(pos, count):
            # base case
            if count == k: 
                if pos == endPos:
                    v = 1
                else:
                    v = 0
                memo[(pos, count)] = v
                return v
            
            # memo
            if (pos, count) in memo:
                return memo[(pos, count)] 
            
            left = dfs(pos - 1, count + 1)
            right = dfs(pos + 1, count + 1)

            memo[(pos, count)] = left + right
            return left + right
        

        memo = {}
        rst = dfs(startPos, 0)
        return rst % (10**9+7)
    
    def method2(self, startPos, endPos, k):
        """
        Combination. 
        Case 1:
            If equal left and right steps, after k steps, must stps at startPos. k must 
            be an even number. And select k//2 steps from k steps is the answer.
        Case 2:
            If left and right steps are not equal. Note small as the steps walked toward
            the direction with smaller steps, and large as the steps walked towared the 
            direction with larger steps. Then the following equation holds:
            diff = abs(startPos - endPos) ------ (1)
            large + small = k             -------(2)
            large - small = diff          -------(3)
            from equations(1) to (3), we have
            large = (k + diff) // 2.
        Two important things: 1) (k + diff) must be even, 2) result equals different ways
        of selecting large from k.
        """
        if startPos == endPos:
            if k % 2 == 1:
                return 0
            rst = math.comb(k, k//2)
            return rst % (10**9+7)
        else:
            diff = abs(startPos - endPos)
            small = min(startPos, endPos)
            large = max(startPos, endPos)
            if (diff + k) % 2 == 1:
                return 0
            rst = math.comb(k, (diff + k)//2)
            return rst % (10 ** 9 +7)
        
    def method3(self, startPos, endPos, k):
        """
        DP with bottom up.
        dp[t][p]: number of ways to reach position p after t steps 
        """
        diff = abs(startPos - endPos)
        if diff > k:
            return 0
        dp = [[0 for _ in range(2 * k + 1)] for _ in range(k + 1)]
        # shift k steps to avoid negative index, all the second index need to add shift
        shift = k
        dp[0][0 + shift] = 1

        for t in range(1, k+1):
            for p in range(-k, k + 1):
                #if 0 <= p - 1 + shift <= k:
                if p - 1 >= -k:
                    dp[t][p + shift] +=  dp[t-1][p - 1 + shift]
                #if 0 <= p + 1 + shift <= k:
                if p + 1 <= k:
                    dp[t][p + shift] += dp[t-1][p + 1 + shift]
        return dp[k][diff+shift] % (10**9+7)