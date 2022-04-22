# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 10:08:08 2020

@author: wyue
"""

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        # if not path:
        #     return path
        # rst = []
        # dot = 0
        # for ele in path:
        #     if ele=='.':
        #         ## signle dot
        #         if dot == 0:
        #             dot = 1
        #             while len(rst) and rst[-1] =='/':
        #                 rst.pop()
        #         ## double dot                            
        #         else:
        #             dot = 1
        #             while len(rst):
        #                 if rst[-1] !='/':
        #                     rst.pop()
        #                 else:
        #                     rst.pop()
        #                     break
        #     elif len(rst)>0 and ele == '/':
        #         dot = 0
        #         if rst[-1] == '/':
        #             continue
        #         else:
        #             rst.append(ele)
        #     else:
        #         dot = 0
        #         rst.append(ele)
                
        # if rst == []:
        #     return '/'
        # elif len(rst)>1 and rst[-1] == '/':
        #     rst.pop()
        # return ''.join(rst)
        rst = []
        path = path.split('/')
        for ele in path:
            ele = ele.strip()
            if ele=='..':
                if len(rst)>0:
                    rst.pop()
            elif ele=='.':
                continue
            elif ele=='':
                continue
            else:
                rst.append(ele)
        
        output = ['/']
        for ele in rst:
            output.append(ele)
            output.append('/')
        if len(output)>1 and output[-1]=='/':
            output.pop()
        return ''.join(output)
    
path = "/../"
print(Solution().simplifyPath(path))