class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(col, row, i):
            if i == len(word):
                return True
            
            if word[i] != board[row][col]:
                return False

            return dfs(col + 1, row, i + 1) or dfs(col - 1, row, i + 1) or dfs(col, row + 1, i + 1) or dfs(col, row - 1, i + 1)
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(c, r, 0) == True:
                    return True
        
        return False