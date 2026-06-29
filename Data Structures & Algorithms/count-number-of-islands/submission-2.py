class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        row_size, col_size = len(grid), len(grid[0])
        answer = 0

        def bfs(r, c):
            coordinates = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))

            while q:
                (r, c) = q.popleft()
                for coords in coordinates:
                    new_r, new_c = r + coords[0], c + coords[1]
                    if new_r < 0 or new_r >= row_size or new_c < 0 or new_c >= col_size or (new_r, new_c) in visited or grid[new_r][new_c] == '0':
                        continue
                    visited.add((new_r, new_c))
                    q.append((new_r, new_c))


        for i in range(row_size):
            for j in range(col_size):
                if grid[i][j] == '1' and (i, j) not in visited:
                    bfs(i, j)
                    answer += 1
        
        return answer
            