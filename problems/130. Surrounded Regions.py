from typing import List
from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.method1(board)
    
    def method1(self, board):
        """
        BFS
        """
        
        M = len(board)
        N = len(board[0])
        
        dq = deque()
        
        ## change 'o' on the border to '-'
        ## top and bottom row
        for col in range(N):
            if board[0][col] == 'O':
                board[0][col] = '-'
                dq.append((0, col))
            if board[M-1][col] == 'O':
                board[M-1][col] = '-'
                dq.append((M-1, col))
        
        ## first and last col
        for row in range(M):
            if board[row][0] == 'O':
                board[row][0] = '-'
                dq.append((row, 0))
            if board[row][N-1] == 'O':
                board[row][N-1] = '-'
                dq.append((row, N-1))
        
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while dq:
            for _ in range(len(dq)):
                row, col = dq.popleft()
                for dr, dc in dirs:
                    if (0 <= row + dr < M) and (0 <= col + dc < N):
                        if board[row+dr][col+dc] == 'O':
                            board[row+dr][col+dc] = '-'
                            dq.append((row+dr, col+dc))

        for row in range(M):
            for col in range(N):
                if board[row][col] == '-':
                    board[row][col] = 'O'
                else:
                    board[row][col] = 'X'
                
if __name__ == '__main__':
    board = [["O","O","O"],["O","O","O"],["O","O","O"]]
    Solution().solve(board)
    print(board)
    
        
        
        