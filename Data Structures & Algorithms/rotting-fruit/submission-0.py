class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        q = collections.deque()
        fresh_count = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    fresh_count += 1
        
        step = 0
        while q and fresh_count > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS) and (0 <= nc < COLS) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        q.append((nr, nc))
            step += 1
            
        
        return step if not fresh_count else -1