# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 23:05:50 2020

@author: wyue
"""

## Vocabulary
valuedic = {'I':1,
       'V':5,
       'X':10,
       'L':50,
       'C':100,
       'D':500,
       'M':1000}

subdic = {'V':'I',
          'X':'I',
          'L':'X',
          'C':'X',
          'D':'C',
          'M':'C'
    }


def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    v = 0
    i = len(s)-1
    sub = False
    subs = ''
    while(i!=-1):
        if sub == True and s[i]==subs:
            v-=valuedic[s[i]]
        else:
            v+=valuedic[s[i]]
        if s[i] == 'V' or s[i] == 'X':
            subs = 'I'
        elif s[i] == 'L' or s[i] == 'C':
            subs = 'X'
        elif s[i] == 'D' or s[i] == 'M':
            subs = 'C'
        if s[i]=='I':
            sub = False
        else:
            sub = True
        i -=1
    return v

roman = 'MCMXCIV'
print(romanToInt(roman))
