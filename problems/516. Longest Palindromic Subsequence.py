
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}
        return self.recursion(s, 0, len(s) - 1, memo)
 
        
    def recursion(self, s, left, right, memo):
        ## Base case 1: two pointers meet
        if left == right:
            return 1
        ## Base case 2: two pointers cross
        if left > right:
            return 0
        ## Base case 3: calculated before
        if (left, right) in memo:
            return memo[(left, right)]
        
        
        if s[left] == s[right]:
            return 2 + self.recursion(s, left + 1, right - 1, memo)
        else:
            leftv = self.recursion(s, left, right - 1, memo)
            rightv = self.recursion(s, left + 1, right, memo)
            maxv = max(leftv, rightv)
            memo[(left, right)] = maxv
            return maxv
        
            