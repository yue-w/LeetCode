# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 23:03:46 2020

@author: wyue
"""
import sys
def longestCommonPrefix(strs):
    # out = ''
    # minlen = -sys.maxsize
    
    # if len(strs) == 1:
    #     return strs[0]
    # elif len(strs) == 0:
    #     return ''
    # else:
    #     for w in strs:
    #         if len(w)<minlen:
    #             minlen = len(w)
    #     same = True
    #     for i in range(minlen):
    #         for j in range(len(strs)-1):
    #             if strs[j][i]!=strs[j+1][i]:
    #                 same = False
    #                 return out
    #         if same == True:
    #             out+=strs[0][i]
    #     return out
    
    out = ''
    if len(strs) == 0:
        return out
    
    for i in range(len(strs[0])):
        char = strs[0][i]
        for j in range(1, len(strs)):
            if i>=len(strs[j]) or char != strs[j][i]:
                return out
        out += char
    return out
    
    

strs = ["ab","a"]
print(longestCommonPrefix(strs))