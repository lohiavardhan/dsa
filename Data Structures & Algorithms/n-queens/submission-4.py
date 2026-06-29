class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        board = [['.' for i in range(n)] for j in range(n)]
        
        cols = set()
        pos_diag = set()
        neg_diag = set()

        res = []

        def dfs(row):
            if row == n:
                curr = ["".join(board[i]) for i in range(n)]
                res.append(curr)
                return
            
            for col in range(n):
                if col not in cols and row + col not in pos_diag and row - col not in neg_diag:
                    board[row][col] = 'Q'
                    cols.add(col)
                    pos_diag.add(row + col)
                    neg_diag.add(row - col)
                    dfs(row + 1)
                    board[row][col] = '.'
                    cols.remove(col)
                    pos_diag.remove(row + col)
                    neg_diag.remove(row - col)

        dfs(0)


        return res