class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        fresh_count = 0
        q = collections.deque()
        coordinates = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh_count += 1
                if grid[i][j] == 2:
                    q.append((i, j, 0))

        while q:
            for _ in range(len(q)):
                row, col, time = q.popleft()
                if fresh_count == 0:
                    return time

                for dr, dc in coordinates:
                    nr = row + dr
                    nc = col + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        q.append((nr, nc, time + 1))


        
        return -1