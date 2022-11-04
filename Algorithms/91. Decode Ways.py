

class Solution:
    def numDecodings(self, s: str) -> int:
        ## the key of len(s) is empty string
        memo = {}
        return self.recursion(s, 0, memo)

    def recursion(self, s, i, memo):
        ## Base case:
        if s[i:] == '':
            memo[''] = 1
            return 1
        if s[i] == '0':
            memo['0'] = 0
            return 0
        if s[i:] in memo:
            return memo[s[i:]]
        
        fst1 = self.recursion(s, i + 1, memo)
        
        if i + 1 < len(s):
            if s[i] == '1' or (s[i] == '2' and int(s[i + 1]) <= 6):
                fst2 = self.recursion(s, i + 2, memo)
                fst1 += fst2
        memo[s[i:]] = fst1
        return fst1
        