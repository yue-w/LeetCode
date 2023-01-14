
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        return self.method2(s)# preferred method
    def method1(self, s):
        n = len(s)
        length = [1] * n
        for i in range(1, n):
            if ord(s[i]) - ord(s[i - 1]) == 1:
                length[i] = length[i-1] + 1
        
        return max(length)
        
    def method2(self, s):
        rst = 1
        curr = 1
        for i in range(1, len(s)):
            if ord(s[i]) - ord(s[i-1]) == 1:
                curr += 1
                rst = max(rst, curr)
            else:
                curr = 1
                
        
        return rst
        