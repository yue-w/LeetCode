
from functools import cache
class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        
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