from collections import defaultdict
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = defaultdict(list)
        for pre in prerequisites:
            dic[pre[1]].append(dic[0])

        for key in dic.keys():
            v = self.recursion(key, dic)
            if v == dic[key]:
                return False
            
        return True
                    
    def recursion(self, v, dic):      
        # Base case
        if v not in dic:
            return v
        else:
            for key in dic[v]:
                return self.recursion(key, dic)

if __name__ == '__main__':
    numCourses = 2
    prerequisites = [[1,0], [0, 3]]
    s = Solution()
    rst = s.canFinish(numCourses, prerequisites)
    print(rst)


