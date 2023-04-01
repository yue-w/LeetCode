# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 17:00:10 2020

@author: wyue
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        table1 = [0] * 26
        table2 = [0] * 26

        for s in s1:
            table1[ord(s) - ord('a')] += 1
        n = len(s1)
        for i in range(len(s2)):
            table2[ord(s2[i]) - ord('a')] += 1
            if i >= n - 1:
                if table1 == table2:
                    return True
                table2[ord(s2[i - n + 1]) - ord('a')] -= 1
        
        return False 
            

s1 = "ab"
s2 = "eidbaooo"
print(Solution().checkInclusion(s1,s2))

