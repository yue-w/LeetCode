
import copy
from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        return self.method1(s) ## BFS
        return self.method2(s) ## DFS. Preferred method
    
        
    def method1(self, s):
        """
        BFS
        Time: O(2^n)
        """
        rst = [[] for _ in range(1)]
        for i in range(len(s)):
            if s[i].isdigit():
                for ele in rst:
                    ele.append(s[i])

            else:
                char = s[i].lower()
                rst2 = copy.deepcopy(rst)
                for ele in rst:
                    ele.append(char)
                for ele in rst2:
                    index = ord(char) - ord('a') + ord('A')
                    ele.append(chr(index))
                rst += rst2
                
        for i in range(len(rst)):
            rst[i] = ''.join(rst[i])
            
        return rst
    
    def method2(self, s):
        """
        DFS.
        Time: O(2^n)
        Space: O(2^n)
        """
        string = [char for char in s]
        rst = []
        self.dfs(rst, string, 0)
        return rst
        
    def dfs(self, rst, string, i):
        ## base case 
        if i == len(string):
            rst.append(''.join(string))
            return
        
        ## if digit, 1 branch
        if string[i].isdigit():
            self.dfs(rst, string, i+1)
        ## if letter, 2 branches
        else:
            ## first branch
            string[i] = string[i].lower()
            self.dfs(rst, string, i + 1)
            ## change letter from upper to lower/ lower to upper
            string[i] = string[i].upper()
            self.dfs(rst, string, i + 1)
            
        
        
if __name__ == '__main__':
    string = "c"
    rst = Solution().letterCasePermutation(string)
    print(rst)