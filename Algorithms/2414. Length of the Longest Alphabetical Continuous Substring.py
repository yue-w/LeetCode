
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        n = len(s)
        length = [1] * n
        for i in range(1, n):
            if ord(s[i]) - ord(s[i - 1]) == 1:
                length[i] = length[i-1] + 1
        
        return max(length)