# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 15:02:09 2020

@author: wyue
"""

class Solution(object):
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return s[left+1:right+1] == s[left+1:right+1][::-1] or s[left:right] == s[left:right][::-1]
            left += 1
            right -= 1
                
        return True