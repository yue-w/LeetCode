

# # from functools import lru_cache
# # from functools import cache
# from functools import cache
class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        
        def dfs(pos, count):
            # base case
            if count == k: 
                if pos == endPos:
                    self.rst += 1
                    v = 1
                else:
                    v = 0
                memo[(pos, count)] = v
                return v
            
            # memo
            if (pos, count) in memo:
                return memo[(pos, count)] 
            
            self.rst += dfs(pos - 1, count + 1)
            self.rst += dfs(pos + 1, count + 1)

        
        self.rst = 0
        memo = {}
        self.rst = dfs(startPos, 0)
        return self.rst

# startPos=1
# endPos=1000
# k=999
startPos=1
endPos=2
k=3
rst = Solution().numberOfWays(startPos, endPos, k)
print(rst)