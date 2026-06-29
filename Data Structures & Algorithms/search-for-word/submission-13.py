class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS = len(board)
        COLS = len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c, curr_word, visited):
            if curr_word == word:
                return True
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or len(curr_word) > len(word) or (r, c) in visited:
                return False
            
            curr_word += board[r][c]
            visited.add((r, c))

            for dr, dc in directions:
                if dfs(r + dr, c + dc, curr_word, visited):
                    return True
        
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, "", set()):
                    return True

        return False