class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited = set()

        def dfs(size, row, col):
            if size == len(word):
                return True
            if size > len(word) or row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or board[row][col] != word[size] or (row,col) in visited:
                return False
            
            visited.add((row,col))
            res = dfs(size + 1, row + 1, col) or dfs(size + 1, row - 1, col) or dfs(size + 1, row, col + 1) or dfs(size + 1, row, col - 1) 
            visited.remove((row,col))

            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(0, i, j):
                    return True
        
        return False