class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        answer = 0
        visited = set()

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visited.add((r,c))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            
            while q:
                (r, c) = q.popleft()
                for dr in directions:
                    (nr, nc) = (r + dr[0], c + dr[1])
                    if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]) or grid[r][c] == '0' or (nr, nc) in visited:
                        continue
                    
                    visited.add((nr, nc))
                    q.append((nr, nc))

                    
            
            

        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1' and (r, c) not in visited:
                    visited.add((r, c))
                    answer += 1
                    bfs(r, c)
                    print(r, c, grid[r][c], visited)
        return answer