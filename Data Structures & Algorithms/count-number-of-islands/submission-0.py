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
                    (r, c) = (r + dr[0], c + dr[1])

                    if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]) and grid[r][c] == '1' and (r, c) not in visited:
                        visited.add((r, c))
                        q.append((r, c))

                    
            
            

        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1' and (r, c) not in visited:
                    
                    visited.add((r, c))
                    answer += 1
                    bfs(r, c)
                    print(r, c, grid[r][c], visited)
        return answer