# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 14:44:28 2020

@author: wyue
"""
from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs) == 1:
            return [strs]
        
        dic = defaultdict(list)
        for word in strs:
            ## sort the word
            word_sorted = ''.join(sorted(word))
            dic[word_sorted].append(word)
        
        ## list comprehension
        return [dic[key] for key in dic]
            


strs = ["eat","tea","tan","ate","nat","bat"]

print(Solution().groupAnagrams(strs))