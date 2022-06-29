# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 21:26:55 2022

@author: wyue
"""

class Solution:
    def findAnagrams(self, s: str, p: str):
        rst = []
        
        ## template table counting chars
        template = [0] * 26
        for char in p:
            template[ord(char) - ord('a')] += 1
        
        ## current table counting chars
        curr = [0] * 26
        for i in range(len(s)):
            curr[ord(s[i]) - ord('a')] += 1
            
            if i >= len(p):
                curr[ord(s[i - len(p)]) - ord('a')] -= 1
                
            if self.same(curr, template):
                rst.append(i - len(p) + 1)

        
        return rst
    
    def same(self, curr, template):
        """
        Return True if curr and template are the same
        """
        
        for i in range(len(curr)):
            if curr[i] != template[i]:
                return False
            
        return True
    

    
if __name__ == '__main__':
    ss = "baa"
    p = "aa"
    s = Solution()
    print(s.findAnagrams(ss, p))
    
    
