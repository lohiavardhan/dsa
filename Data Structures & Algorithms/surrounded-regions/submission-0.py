class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(i, j):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or board[i][j] != 'O':
                return 
            
            board[i][j] = '#'

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        for r in range(ROWS):
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][COLS - 1] == 'O':
                dfs(r, COLS - 1)
        
        for c in range(COLS):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[ROWS - 1][c] == 'O':
                dfs(ROWS - 1, c)
        

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'
                
            