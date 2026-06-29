class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS = len(board)
        COLS = len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()

        def dfs(r, c, size):
            if size == len(word):
                return True
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or size > len(word) or (r, c) in visited or board[r][c] != word[size]:
                return False
            

            visited.add((r, c))
            for dr, dc in directions:
                if dfs(r + dr, c + dc, size + 1):
                    return True
            visited.remove((r, c))
        
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0):
                    return True

        return False