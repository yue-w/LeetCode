from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        Step 1: construct a DP table to lookup
        dp[i][j]: whether the substring from s[i] to s[j] is parlindrome.
        """
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        
        
        ## initialize dp for boundary conditions
        for i in range(len(s)):
            dp[i][i] = True
        
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
        
        ## length is the length of the sub string
        ## i is start, j is end, j = i - len + 1
        ## all indexes below in the form of dp[a][b] should have a <= b
        ## this makes length >= 3
        for length in range(3, len(s) + 1):
            curr = []
            i = 0
            j = i + length - 1
            while j < len(s):
                j = i + length - 1
                ## DP
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                else:
                    dp[i][j] = False
                i += 1
                j = i + length - 1
                    
        """
        Step 2: call dfs to get palindromes
        """
        rst = []
        curr = []
        self.dfs(0, s, curr, rst, dp)
        
        return rst
        
    def dfs(self, i, s, curr, rst, dp):
        ## Base case
        if i == len(s):
            rst.append(curr[:])
            return 
            
        for j in range(i, len(s)):
            if dp[i][j]:
                curr.append(s[i:j+1])
                self.dfs(j + 1, s, curr, rst, dp)
                curr.pop()
        
if __name__ == '__main__':
    s = Solution()
    string = "efe"
    print(s.partition(string))