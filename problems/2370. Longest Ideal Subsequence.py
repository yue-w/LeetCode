
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        #return self.method1(s, k)## my initial solution
        return self.method2(s, k)
        
    def method1(self, s, k):
        """
        My initial solution in the contest. 
        Use dictionary to store the last occurance of each char.
        Build a table to look up the chars within distance k.
        time: O(n)
        """
        def get_k(char):
            chars = [char]
            ## go right:
            i = 1
            while i <= k and chr(ord(char) + i) <= 'z':
                chars.append(chr(ord(char) + i))
                i += 1
            ## go left
            i = -1
            while i >= -k and chr(ord(char) + i) >= 'a':
                chars.append(chr(ord(char) + i))
                i -= 1
                
            return chars
        
        tables = []
        for i in range(26):
            tables.append(get_k(chr(ord('a') + i))) 
        
        dic = {}
        
        for char in s:
            maxv = 1
            for c in tables[ord(char) - ord('a')]:
                if c in dic:
                    maxv = max(maxv, dic[c] + 1)
            dic[char] = maxv
        
        rst = 0
        for v in dic.values():
            rst = max(rst, v)
        return rst
    
    def method2(self, s, k):
        """
        Similar to mehtod1, but using template.
        State machine. DP.
        """
        ## use a table to record the last occurance index for
        ## each of the 26 characters. -1 if no occurance yet. (state machine)
        last_occ = [-1] * 26
        ## dp[i] the length of the longest ideal string ending with s[i].
        dp = [1] * len(s)
        
        for i in range(len(s)):
            ## for each of the chars witihin distance k from s[i]
            for ch in range(max(0, ord(s[i]) - ord('a') - k), min(25, ord(s[i]) - ord('a') + k) +1 ):
                j = last_occ[ch]
                if j != -1:
                    dp[i] = max(dp[i], dp[j] + 1) 
            
            last_occ[ord(s[i]) - ord('a')] = i
        
        return max(dp)
        
        