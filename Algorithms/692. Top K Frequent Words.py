# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 21:09:43 2020

@author: wyue
"""
import heapq
import collections
from typing import List

class Element:
    def __init__(self, count, word):
        self.count = count
        self.word = word
        
    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count
    
    def __eq__(self, other):
        return self.count == other.count and self.word == other.word

class Solution:
    """
    Time: O(nlogk)
    Space: O(n)
    """
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        #return self.method1(words, k)
        return self.method2(words, k) # preferred method
    
    def method1(self, words, k):
        """
        Customerize a class
        """
        counts = collections.Counter(words)   
        
        freqs = []
        for word, count in counts.items():
            if len(freqs) < k:
                heapq.heappush(freqs, Element(count, word))
            
            else:
                ## use constant time to check the smallest element in the heap, heappush and heappop if
                ## necessary.
                if count > freqs[0].count or (count == freqs[0].count and word < freqs[0].word):
                    ## heappushpop is more efficient than heappush followed by heappop
                    heapq.heappushpop(freqs, Element(count, word))
                    
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(freqs).word)
        return res[::-1]
    
    def method2(self, words, k):
        """
        Same method, but does not need a customerized class
        """
        import heapq
        from collections import Counter
        counter = Counter(words)
        hq = []
        for word, count in counter.items():
            heapq.heappush(hq, (-count, word))
        rst = []
        for _ in range(k):
            rst.append(heapq.heappop(hq)[1])
        return rst
    
words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2

print(Solution().topKFrequent(words,k))