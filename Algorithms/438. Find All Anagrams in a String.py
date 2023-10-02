# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 21:26:55 2022

@author: wyue
"""

class Solution:
    def findAnagrams(self, s: str, p: str):
        """
        Moving (fixed) window
        """
        rst = []
        pp = [0] * 26
        ss = [0] * 26

        for char in p:
            idx = ord(char) - ord('a')
            pp[idx] += 1
        
        for i in range(len(s)):
            idx = ord(s[i]) - ord('a')
            ss[idx] += 1
            if i >= len(p):
                j = i - len(p)
                ss[ord(s[j]) - ord('a')] -= 1
            if ss == pp:
                rst.append(i - len(p) + 1)
 
        return rst
    

    
if __name__ == '__main__':
    ss = "baa"
    p = "aa"
    s = Solution()
    print(s.findAnagrams(ss, p))
    
    
