# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 16:02:03 2020

@author: wyue
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s)-1
        
        while i<j:
            ## If not alphanumeric characters, ignore
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            if s[i].lower()!=s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        
        return True
s  = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))