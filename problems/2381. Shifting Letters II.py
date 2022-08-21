
from typing import List
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        """
        Template for sweeping line/ diff array.
        Reference: https://youtu.be/IzDbDlzvH2M
        """
        n = len(s)
        
        ## for n elements, we need (n + 1) diff
        diff = [0] * (n+1)
        for start, end, direc in shifts:
            
            if direc == 1:
                delta = 1
            else:
                delta = -1
            diff[start] += delta
            diff[end+1] -= delta
            
        curr = 0
        print(diff)
        string = [c for c in s]  
        for i in range(len(s)):
            curr += diff[i]
            ## move is the relative index from 'a', and move should be between 0 and 25
            move = (ord(string[i]) - ord('a') + curr % 26 + 26) % 26
            string[i] = chr(move + ord('a'))
            
        return ''.join(string)