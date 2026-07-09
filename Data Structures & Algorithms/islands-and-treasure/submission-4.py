class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = set()

        q = collections.deque()
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i, j, 0))
                    visited.add((i, j))

        while q:
            for _ in range(len(q)):
                print('here')
                curr_row, curr_col, curr_num = q.popleft()
                for dr, dc in directions:
                    nr, nc = curr_row + dr, curr_col + dc
                    if nr < ROWS and nr >= 0 and nc < COLS and nc >= 0 and grid[nr][nc] != -1 and (nr, nc) not in visited:
                        grid[nr][nc] = min(grid[nr][nc], curr_num + 1)
                        visited.add((nr, nc))
                        q.append((nr, nc, curr_num + 1))
        
        #return grid



        
