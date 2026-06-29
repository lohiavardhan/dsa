class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        answer_list = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        
        col_set = set()
        posDiag = set()
        negDiag = set()      

        curr_list = []

        def dfs(curr_row):
            if curr_row >= n:
                curr_list = []
                for i in range(n):
                    curr_list.append("".join(board[i]))
                answer_list.append(curr_list)
                return
            
            for col in range(n):
                if col not in col_set and (col + curr_row) not in posDiag and (curr_row - col) not in negDiag:
                    col_set.add(col)
                    posDiag.add(col + curr_row)
                    negDiag.add(curr_row - col)
                    board[curr_row][col] = "Q"
                    dfs(curr_row + 1)

                    board[curr_row][col] = "."
                    col_set.remove(col)
                    posDiag.remove(col + curr_row)
                    negDiag.remove(curr_row - col)
                

        dfs(0)     
        return answer_list
        