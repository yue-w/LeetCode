from typing import List 


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ## if the last letter is smaller than target, return the first letter (because the letters wrap around)
        if letters[-1] <= target:
            return letters[0]
        
        left = 0
        right = len(letters) - 1
        while left < right:
            mid = left + (right - left) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return letters[left]