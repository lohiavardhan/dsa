class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set()
        frontier = []
        cost = 0
        heapq.heappush(frontier, (grid[0][0], 0, 0))
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while True:
            curr_cost, i, j = heapq.heappop(frontier)
            
            cost = max(curr_cost, cost)
            if (i, j) in visited:
                continue
            if i == ROWS - 1 and j == COLS - 1:
                return cost
            
            visited.add((i, j))

            for dr, dc in directions:
                newr, newc = i + dr, j + dc
                if newr < ROWS and newr >= 0 and newc < COLS and newc >= 0:
                    heapq.heappush(frontier, (grid[newr][newc], newr, newc))
