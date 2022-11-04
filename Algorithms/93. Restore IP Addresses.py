
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        return self.method1(s)
        
    def method1(self, s):
        """
        dfs, backtracking
        """
        rst = []
        curr = []
        self.dfs(rst, curr, 0, s)
        return rst
        
    def dfs(self, rst, curr, index, s):
        ## base case
        if index == len(s): 
            if len(curr) == 4:
                rst.append('.'.join(curr))
            return 
        if len(curr) == 4 and index < len(s):
            return
        
        for i in range(1, 4):
            tem = s[index: index + i]
            if not tem:
                return 
            if (len(tem) > 1 and tem[0] == '0') or int(tem) > 255:
                return
            curr.append(tem)
            self.dfs(rst, curr, index + i, s)
            ## backing track
            curr.pop()

if __name__ == '__main__':
    s = "25525511135"
    rst = Solution().restoreIpAddresses(s)
    print(rst)