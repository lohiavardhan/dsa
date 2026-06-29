class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c, curr_area):
            nonlocal res
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return
            
            res = max(res, curr_area)
            grid[r][c] = 0
            for [dr, dc] in directions:
                dfs(r + dr, c + dc, curr_area + 1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    dfs(i, j, 1)
        
        return res