class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        INF = 2147483647
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def bfs(r, c):
            visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
            q = collections.deque()
            q.append((r, c))
            steps = 0

            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()
                    if grid[row][col] == 0:
                        return steps
                    
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        if (0 <= nr < ROWS) and (0 <= nc < COLS) and (not visited[nr][nc]) and (grid[nr][nc] != -1):
                            visited[nr][nc] = True
                            q.append((nr, nc))
                    
                steps += 1
            
            return INF
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == INF:
                    grid[i][j] = bfs(i, j)