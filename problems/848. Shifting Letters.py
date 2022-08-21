from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        """
        Time: O(n)
        """
        total = sum(shifts)
        n = len(s)
        strings = [char for char in s]
        for i in range(n):
            idx = (ord(strings[i]) - ord('a') + (total % 26) + 26) % 26
            strings[i] =  chr(idx + ord('a'))
            total -= shifts[i]
            
        return ''.join(strings)