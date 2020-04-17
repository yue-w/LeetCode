# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 23:04:33 2020

@author: wyue
"""

"""
## A straight forward method
left = {'(':')',
        '{':'}',
        '[':']'}

right = {')':'(',
         '}':'{',
         ']':'['}

def isValid(s):
    length = len(s)
    if length == 0:
        return True
    if length%2==1:
        return False
    

    while(len(s)>1):
        if s[-1] in left:
            return False
        for i in range(1,len(s)):
            if s[i] in left:
                continue
            if s[i-1]==right[s[i]]:
                s = s[:i-1]+s[i+1:]
                break
            else:
                return False
    return True
"""

right = {')':'(',
         '}':'{',
         ']':'['
         }

def isValid(ss):
    stack = []
    for char in ss:
        if char in right: 
            poped = stack.pop() if stack else ''
            if poped != right[char]:
                return False
        else:
            stack.append(char)
    return not stack
ss = '(('  
print(isValid(ss))
