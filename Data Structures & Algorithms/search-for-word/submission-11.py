class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        path = set()

        def dfs(size, i, j):
            if size == len(word):
                return True
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[size] or (i, j) in path:
                return False
            
            path.add((i, j))
            res = dfs(size + 1, i + 1, j) or dfs(size + 1, i - 1, j) or dfs(size + 1, i, j + 1) or dfs(size + 1, i, j - 1)
            path.remove((i, j))

            return res
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(0, i, j):
                    return True
        
        return False