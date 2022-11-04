
from collections import defaultdict
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowdic = defaultdict(set)
        coldic = defaultdict(set)
        griddic = defaultdict(set)
        
        for row in range(9):
            for col in range(9):
                char = board[row][col]
                if char == '.':
                    continue
                if (char in rowdic[row] or
                    char in coldic[col] or
                    char in griddic[(row // 3, col // 3)]
                   ): 
                    return False
                rowdic[row].add(char)
                coldic[col].add(char)
                griddic[(row//3, col//3)].add(char)
        return True