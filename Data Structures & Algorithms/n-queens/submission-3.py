class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        rows = set()
        cols = set()
        pos_diags = set()
        neg_diags = set()

        res = []

        def dfs(r, num_queen, curr_path):
            print(curr_path)
            if num_queen == n:
                curr_res = []
                for i in range(n):
                    curr_res.append("".join(curr_path[i]))

                res.append(curr_res.copy())
                return
            
            i = r
            for j in range(n):
                if (i not in rows) and (j not in cols) and ((i + j) not in pos_diags) and ((i - j) not in neg_diags):
                    curr_path[i][j] = 'Q'
                    rows.add(i)
                    cols.add(j)
                    pos_diags.add(i + j)
                    neg_diags.add(i - j)
                    dfs(i + 1, num_queen + 1, curr_path)
                    curr_path[i][j] = '.'
                    rows.remove(i)
                    cols.remove(j)
                    pos_diags.remove(i + j)
                    neg_diags.remove(i - j)
        
        path = [['.' for i in range(n)] for j in range(n)]
        
        dfs(0, 0, path)

        return res