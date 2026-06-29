class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        col = set()
        posDiag = set() # r + c
        negDiag = set() # r - c

        board = [["."] * n for i in range(n)]
        print(board)
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return
            
            for c in range(n):
                if(c in col or (c+r) in posDiag or (r - c) in negDiag):
                    continue
                
                col.add(c)
                posDiag.add(c + r)
                negDiag.add(r - c)
                board[r][c] = 'Q'

                backtrack(r + 1)

                col.remove(c)
                posDiag.remove(c + r)
                negDiag.remove(r - c)
                board[r][c] = '.'
        
        backtrack(0)
        return result
