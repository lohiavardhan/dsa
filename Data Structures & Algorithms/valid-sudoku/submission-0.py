class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        
        
        for i in range(len(board)):
            column = set()
            for j in range(len(board)):
                if board[i][j] == '.':
                    continue
                if board[i][j] in column:
                    print('here1', board[i][j], i, j, column)
                    return False
                else:
                    column.add(board[i][j])
        
        for j in range(len(board)):
            row = set()
            for i in range(len(board)):
                if board[i][j] == '.':
                    continue
                if board[i][j] in row:
                    print('here2')
                    return False
                else:
                    row.add(board[i][j])
        
        start_row = 0
        start_col = 0

        while True:
            
            curr_space = set()

            end_row = start_row + 3
            end_col = start_col + 3

            for i in range(start_row, end_row):
                for j in range(start_col, end_col):
                    if board[i][j] == '.':
                        continue
                    if board[i][j] in curr_space:
                        print('here3')
                        return False
                    else:
                        curr_space.add(board[i][j])

            
            if start_col < 6:
                start_col += 3
                start_row = start_row
            else:
                start_row += 3
                start_col = 0

            if start_row > 7:
                break
        
        return True

            
