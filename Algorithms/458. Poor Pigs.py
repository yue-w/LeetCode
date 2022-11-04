
import math
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        """
        Reference: https://leetcode.com/problems/poor-pigs/discuss/94273/Solution-with-detailed-explanation
        """
        times = minutesToTest // minutesToDie
        rst = math.log(buckets, times + 1)
        rst = int(math.ceil(rst))
        return rst
        
        

if __name__ == '__main__':
     buckets = 5
     minutesToDie = 15
     minutesToTest = 20  
     rst = Solution().poorPigs(buckets, minutesToDie, minutesToTest)
     print(rst)