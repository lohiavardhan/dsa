class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ROWS = len(grid)
        COLS = len(grid[0])
        INF = 2147483647
        visited = set()

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == -1 or (r, c) in visited:
                return INF
            if grid[r][c] == 0:
                return 0
            
            visited.add((r, c))
            res = 1 + min(dfs(r + 1, c), dfs(r - 1, c), dfs(r, c + 1), dfs(r, c - 1))
            visited.remove((r, c))

            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    grid[r][c] = dfs(r, c)
