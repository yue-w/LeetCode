from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        return self.two_pointers(height)

    def brute_force(self, height):
        """
        sliding window/ two pointers
        Bruteforce O(n^2)
        """
        maxA = 0
        for left in range(0, len(height) - 1):
            for right in range(left + 1, len(height)):
                area = min(height[left], height[right]) * (right - left)
                maxA = max(maxA, area)
        return maxA
    
    def two_pointers(self, height):
        left = 0
        right = len(height) - 1
        max_a = 0
        
        while left < right:
            max_a = max(max_a, min(height[right], height[left]) * (right - left))
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
                
        return max_a


