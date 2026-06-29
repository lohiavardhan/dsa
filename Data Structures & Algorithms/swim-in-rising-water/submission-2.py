class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        visited = set()
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        frontier = []
        heapq.heappush(frontier, (grid[0][0], 0, 0))

        while True:
            curr_cost, curr_x, curr_y = heapq.heappop(frontier)
            print(frontier, curr_x, curr_y)
            if (curr_x, curr_y) in visited:
                continue
            if (curr_x == len(grid) - 1 and curr_y == len(grid[0]) - 1):
                return curr_cost
            
            visited.add((curr_x, curr_y))

            for dr, dc in directions:
                next_x, next_y = curr_x + dr, curr_y + dc
                if next_x >= 0 and next_x < len(grid) and next_y >= 0 and next_y < len(grid[0]) and (next_x, next_y) not in visited:
                    heapq.heappush(frontier, (max(curr_cost, grid[next_x][next_y]), next_x, next_y))

