
from re import L
from typing import List



class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        #return self.brute_force(height)
        #return self.dp(height)
        return self.two_pointers(height)
    def brute_force(self, height):
        """
        time: O(n^2)
        space: O(1)
        """
        rst = 0
        for current in range(len(height)):
            maxl = 0
            maxr = 0
            
            ## search max height to the left (self included)
            for left in range(0, current + 1):
                maxl = max(maxl, height[left])
                
            ## search max height to the right (self included)
            for right in range(current, len(height)):
                maxr = max(maxr, height[right])
                ## add the following condition to end earlier.
                if maxr > maxl:
                    break
            
            ## height of wall
            h = min(maxl, maxr)
            rst += h - height[current]
            
        return rst

    def dp(self, height):
        ## save max height to the left
        #assert len(height) >= 1, "Lengh of height should not be smaller than 1"
        left_max = [0] * len(height)
        left_max[0] = height[0]
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i - 1], height[i])

        right_max = [0] * len(height)
        right_max[-1] = height[-1]
        for i in range(-2, - len(height) - 1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        rst = 0
        for i in range(len(height)):
            rst += min(left_max[i], right_max[i]) - height[i]

    def two_pointers(self, height):
        left = 0
        right = len(height) - 1
        rst = 0
        left_max = height[0]
        right_max = height[-1]
        while left < right:
            if left_max < right_max:
                rst += left_max - height[left]
                left += 1
                left_max = max(left_max, height[left])
                
            else:
                rst += right_max - height[right]
                right -= 1
                right_max = max(right_max, height[right])
                
        
        return rst


        

if __name__ == '__main__':
    s = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    #height = [4,2,0,3,2,5]
    print(s.trap(height))
