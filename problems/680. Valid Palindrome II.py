# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 15:02:09 2020

@author: wyue
"""

class Solution(object):
    ### Method 1 (My fist approach): Recursion, slower
    """
    def validPalindrome(self, s):

        DELE = False
        return self.helper(s, 0, len(s)-1, DELE)

    def helper(self, s, left, right, DELE):
        if left>=right:
            return True
        else :
            leftChar = s[left]
            rightChar = s[right]
            if leftChar != rightChar:
                if  DELE==True:
                    return False
                else:
                    DELE = True
                    return self.helper(s, left+1, right, DELE) or self.helper(s, left, right-1, DELE) 
            else:
                return self.helper(s, left+1, right-1, DELE)
    """
    #### Method 2 (answer online): Iteration, faster
    def validPalindrome(self, s):
        left =  0
        right = len(s)-1
        while left<=right:
            if s[left] != s[right]:
                return self.isValid(left+1, right, s) or self.isValid(left, right-1, s)
            else:
                left += 1
                right -= 1
        return True
    
    
    def isValid(self, left, right, s):
        while left<=right:
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
            
        return True