# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 14:44:28 2020

@author: wyue
"""
from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Solution 1:
        Time: O(nk)
        """
        seen = defaultdict(list)
        for s in strs:
            table = [0] * 26
            for char in s:
                table[ord(char) - ord('a')] += 1
            seen[tuple(table)].append(s)
        return seen.values()

        """
        Solution 2:
        Time: O(nklogk)
        """
        dic = defaultdict(list)
        for chars in strs:
            chars_sorted = ''.join(sorted(chars))
            dic[chars_sorted].append(chars) 
        return [val for _,val in dic.items()]
            


strs = ["eat","tea","tan","ate","nat","bat"]

print(Solution().groupAnagrams(strs))