# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 21:26:55 2022

@author: wyue
"""

class Solution:
    def findAnagrams(self, s: str, p: str):
        rst = []
        if len(s) < len(p):
            return rst
        
        ## An array to store the count occurance of each of the char.
        ## Array for p will initialized once and then fixed. 
        ## Array for s will be updated using the moving window.
        count_s = [0] * 26
        count_p = [0] * 26
        
        ## Initialize count for p and s.
        for i in range(len(p)):
            index = ord(p[i]) - ord('a')
            count_p[index] += 1
        
        ## Initialize count p
        for i in range(len(p)):
            index = ord(s[i]) - ord('a')
            count_s[index] += 1
        
        if self.are_same(count_s, count_p):
            rst.append(0)
        
        ## Moving window to update count for s.
        for j in range(len(p), len(s)):
            index = ord(s[j]) - ord('a')
            count_s[index] += 1
            index = ord(s[j - len(p)]) - ord('a')
            count_s[index] -= 1
            if self.are_same(count_s, count_p):
                rst.append(j - len(p) + 1)
        
        return rst


    def are_same(self, count1, count2):
        for i in range(26):
            if count1[i] != count2[i]:
                return False
        return True
    

    
if __name__ == '__main__':
    ss = "baa"
    p = "aa"
    s = Solution()
    print(s.findAnagrams(ss, p))
    
    
