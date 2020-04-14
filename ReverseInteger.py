# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 21:42:43 2020

@author: wyue
Given a 32-bit signed integer, reverse digits of an integer.
Note:
Assume we are dealing with an environment which could only store integers 
within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose of
 this problem, assume that your function returns 0 when the reversed integer overflows.
"""

def f(x):
    """
    :type x: int
    :rtype: int
    """
    limits = pow(2,31)

    neg = False
    if x<0:
        x = -x
        neg = True

    rst = 0
    while x>=10:
        ld = x%10
        rst = rst*10+ld
        x = x//10
    rst = rst*10+x
    if neg ==True:
      if rst>limits:
        return 0
      else:
        return -rst
    else:
      if rst>limits-1:
        return 0
      else:
        return rst

print(f(123456))