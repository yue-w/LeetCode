# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 11:12:06 2020

@author: wyue
https://leetcode.com/problems/maximal-network-rank/
"""

import heapq
class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        if not roads:
            return 0
        dic = {}
        for e in roads:
            if e[0] in dic:
                dic[e[0]].append(e[1])
            else:
                dic[e[0]] = [e[1]]
            
            if e[1] in dic:
                dic[e[1]].append(e[0])
            else:
                dic[e[1]] = [e[0]]  

        candidate = []
        lengths = [(-len(dic[i]),i) for i in dic.keys()]
        heapq.heapify(lengths)
        max_Length1, maxNode1 = heapq.heappop(lengths)
        max_Length1 = -max_Length1
        candidate.append((max_Length1,maxNode1))

        max_Length2, maxNode2 = heapq.heappop(lengths)
        max_Length2 = -max_Length2
        candidate.append((max_Length2, maxNode2))
        
        while lengths:
            max_Length, maxNode = heapq.heappop(lengths)
            if -max_Length<max_Length2:
                break
            else:
                candidate.append((-max_Length, maxNode))
        v = 0
        
        for i in range(len(candidate)-1):
            len1, node1 = candidate[i]
            for j in range(i+1,len(candidate)):
                len2, node2 = candidate[j]
                if node2 in dic[node1]:
                    runningV = len1 + len2 - 1
                else:
                    runningV = len1 + len2
                if runningV>v:
                    v = runningV
        return v

        

n = 8
roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
"""
n = 5
roads = [[2,3],[0,3],[0,4],[4,1]]
"""
print(Solution().maximalNetworkRank(n,roads))
