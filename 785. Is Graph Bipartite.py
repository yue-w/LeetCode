# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 16:05:42 2020

@author: wyue
"""

class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        ## DFS
        color = {}
        
        stack = []
        
        
        
        
        # left = set()
        # right = set()
        
        # for tail, heads in enumerate(graph):
        #     if tail in left:
        #         current = left
        #         other = right

        #     elif tail in right:
        #         current = right
        #         other  = left
        #     else:

        #         for head in heads:
        #             if head in left:
        #                 right.add(tail)
        #                 current = right
        #                 other = left
        #                 break
        #             elif head in right:
        #                 left.add(tail)
        #                 current = left
        #                 other = right
        #                 break
        #             else:
        #                 left.add(tail)
        #                 current = left
        #                 other = right
        #                 break
                        
        #     for head in heads:
        #         if not (head in current):
        #             other.add(head)
        #         else:
        #             return False

        # return True
    
graph = [[1],[0,3],[3],[1,2]]
print(Solution().isBipartite(graph))