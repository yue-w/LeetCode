# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 10:08:08 2020

@author: wyue
"""

from re import L


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        return self.method1(path)
    def method1(self, path):
        stack = []
        curr = ''
        path = path + '/'

        for e in path:
            if e == '/':
                if curr == '..':
                    if stack:
                        stack.pop()
                elif curr and curr != '.':
                    stack.append(curr)
                curr = ''
            else:
                curr += e

        return '/' + '/'.join(stack)
        
    def method2(self, path):
        stack = []
        stack.append('/')
        n = len(path)
        i = 0
        while i < n:
            if path[i] == '/':
                if stack[-1] == '/':
                    i += 1
                    continue
                else:
                    stack.append('/')
                    i += 1
                    
            elif path[i] == '.':
                # ## if this dot is not followed by '.' or /, it is part of a folder/file name
                # if i + 1 < n and path[i + 1] not in ['/', '.']:
                #     stack.append('.')
                #     i += 1
                #     continue
                ## this dot is not part of a folder/ file name
                j = i
                while i < n and path[i] == '.':
                    i += 1
                if i < n and (path[i] != '/' or stack[-1] != '/'):
                    while j < i:
                        stack.append(path[j])
                        j += 1
                ## two dots, go up one level if possible
                if i - j == 2:
                    if len(stack) == 1:
                        continue
                    else:
                        stack.pop()
                    while len(stack) > 1 and stack[-1] != '/':
                        stack.pop()
                ## one dot, ignore
                elif i - j  == 1:
                    continue
                ### more than two dots, it is a file/folder name, keep.
                else:
                    while j < i:
                        stack.append(path[j])
                        j += 1
                                    
            else:
                stack.append(path[i])
                i += 1
                
        if stack[-1] == '/' and len(stack) > 1:
            stack.pop()
        
        return ''.join(stack)
        



if __name__ == '__main__':
    s = Solution()
    path = "/a//b////c/d//././/.."
    print(s.simplifyPath(path))