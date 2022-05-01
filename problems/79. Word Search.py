
import copy
from collections import defaultdict
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        for i in range(row):
            for j in range(col):
                run_rst = self.recursion(board, word, i, j, row, col) 
                if run_rst:
                    return True 
        return False
        
    def recursion(self, board, remain_word, i, j, row, col):
        # Base case
        if not remain_word:
            return True
        if i < 0 or j < 0 or i >= row or j >= col:
            return False 
        if board[i][j] != remain_word[0]:
            return False 
        ## the same letter cell cannot be used twice, set it to an unusable to avoid 
        ## double count
        ch_copy = board[i][j]
        board[i][j] = None
        # Search up down left right
        if self.recursion(board, remain_word[1:], i-1, j, row, col):
            return True
        if self.recursion(board, remain_word[1:], i+1, j, row, col):
            return True 
        if self.recursion(board, remain_word[1:], i, j-1, row, col):
            return True
        if self.recursion(board, remain_word[1:], i, j+1, row, col):
            return True
        
        board[i][j] = ch_copy
        return False

            
                    
if __name__ == '__main__':
    s = Solution()
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    rst = s.exist(board, word)
    print(rst)
