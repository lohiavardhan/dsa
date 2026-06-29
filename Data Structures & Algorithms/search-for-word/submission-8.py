class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(curr, i, j):
            if curr == word:
                return True
            if i >= len(board) or j >= len(board[0]) or i < 0 or j < 0:
                return False
            
            if i + 1 < len(board):
                if dfs(curr + board[i + 1][j], i + 1, j):
                    return True
            if i - 1 >= 0:
                if dfs(curr + board[i - 1][j], i - 1, j):
                    return True
            if j + 1 < len(board[0]):
                if dfs(curr + board[i][j + 1], i, j + 1):
                    return True
            if j - 1 >= 0:
                if dfs(curr + board[i][j - 1], i, j - 1):
                    return True
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(board[i][j], i, j):
                    return True
        
        return False