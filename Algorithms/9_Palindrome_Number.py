# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 22:57:47 2020

@author: wyue
"""

def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x<0:
        return False
    else:
        num_x = 1
        xx = x
        while(xx//10>0):
            num_x +=1
            xx = xx//10
        left = 0
        right = num_x-1
        
        while(left<right):
            j = num_x-left-1
            num_left = x//(10**j)%10
            num_right = x//(10**left)%10
            left+=1
            right-=1
            if num_left!=num_right:
                return False
        return True
print(isPalindrome(10))