class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS = len(heights)
        COLS = len(heights[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        pac = set()
        ant = set()

        def dfs(i, j, curr_set, prev_val):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or (i, j) in curr_set or heights[i][j] < prev_val:
                return
            
            curr_set.add((i, j))

            for dr, dc in directions:
                dfs(i + dr, j + dc, curr_set, heights[i][j])
            

        for i in range(ROWS):
            if (i, 0) not in pac:
                dfs(i, 0, pac, heights[i][0])
            
            if (i, COLS - 1) not in ant:
                dfs(i, COLS - 1, ant, heights[i][COLS - 1])
        
        for i in range(COLS):
            if (0, i) not in pac:
                dfs(0, i, pac, heights[0][i])
            
            if (ROWS - 1, i) not in ant:
                dfs(ROWS - 1, i, ant, heights[ROWS - 1][i])
        
        res = []

        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) in pac and (i, j) in ant:
                    res.append([i, j])
        
        return res

        